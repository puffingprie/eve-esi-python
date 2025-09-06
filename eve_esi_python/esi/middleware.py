import time
import threading
import logging
from typing import Dict, Tuple, Callable, Optional

from eve_esi_python.rest import RESTResponse
from eve_esi_python.esi_client.constants import (
    UNAUTHORIZED_STATUS_CODE,
    MAX_REQUESTS_PER_SECOND,
    MAX_RETRIES,
    BACKOFF_FACTOR,
)

LOGGER = logging.getLogger(__name__)


class RateLimitMiddleware:
    def __init__(self, max_requests_per_second: float = MAX_REQUESTS_PER_SECOND):
        self.max_requests_per_second = max_requests_per_second
        self.min_interval = 1 / self.max_requests_per_second
        self.last_request_time: float = 0
        self._lock = threading.Lock()

    def process_request(
        self, method: str, url: str, headers: Dict[str, str], body: Optional[str] = None
    ) -> Tuple[str, str, Dict[str, str], Optional[str]]:
        """
        Process the request and apply rate limiting.

        :return: Returns the `method`, `url`, `headers`, and `body` after applying rate limiting.
        """
        with self._lock:
            curr_time = time.time()
            time_last_since = curr_time - self.last_request_time
            if time_last_since < self.min_interval:
                sleep_time = self.min_interval - time_last_since
                LOGGER.debug(f"Rate limit hit, sleeping for {sleep_time:.2f} seconds")
                time.sleep(sleep_time)
        return method, url, headers, body


class TokenRefreshMiddleware:
    def __init__(self, callback: Optional[Callable[[], str]] = None):
        self.callback = callback
        self._refresh_lock = threading.Lock()

    def process_response(
        self, response: RESTResponse, request_time: float
    ) -> RESTResponse:
        if response.status == UNAUTHORIZED_STATUS_CODE and self.callback:
            LOGGER.debug("Unauthorized response received, attempting to refresh token")
            with self._refresh_lock:
                try:
                    new_token = self.callback()
                    LOGGER.info(
                        f"Token refreshed successfully at {time.time() - request_time:.2f} seconds"
                    )
                except Exception as e:
                    LOGGER.error(f"Token refresh failed: {e}")
                    raise e
        return response


class RetryMiddleware:
    def __init__(
        self, max_retries: int = MAX_RETRIES, backoff_factor: float = BACKOFF_FACTOR
    ):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def handle_errors(
        self, exception: Exception, attempt: int, max_attempts: int
    ) -> bool:
        if attempt < max_attempts:
            wait_time = self.backoff_factor * (2 ** (attempt - 1))
            LOGGER.warning(
                f"Request failed (attempt {attempt}/{max_attempts}): {exception}"
            )
            LOGGER.info(f"Retrying in {wait_time:.2f}s")
            time.sleep(wait_time)
            return True
        return False
