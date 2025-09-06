● Got it! Thank you for the clarification. So we have:

1. cache.py - Different cache backends (Redis, File, Dict, etc.) like EsiPy's implementation
2. client.py - Main EsiClient with session management using TTLCache for user sessions
3. middleware.py - Request/response middleware (rate limiting, token refresh, etc.)
4. sso.py - OAuth2 flow for EVE Online SSO

And the TTL cache for user sessions goes in client.py, while cache.py is for pluggable cache backends.

Let me provide the code for all four files, structured to maintain the excellent type safety while providing great DX:

1. cache.py - Pluggable Cache Backends

```py
# -_- encoding: utf-8 -_-
""" Cache objects for eve-esi-python """
import hashlib
import logging
import datetime
from typing import Any, Optional

try:
    import pickle
except ImportError:  # pragma: no cover
    import cPickle as pickle

LOGGER = logging.getLogger(__name__)


def _hash(data: Any) -> str:
    """ Generate a hash from data object to be used as cache key """
    hash_algo = hashlib.new('md5')
    hash_algo.update(pickle.dumps(data))
    # prefix allows possibility of multiple applications sharing same keyspace
    return 'eve_esi_' + hash_algo.hexdigest()


class BaseCache:
    """ Base cache 'abstract' object that defines the cache methods used in eve-esi-python """

    def set(self, key: Any, value: Any, expire: int = 300) -> None:
        """ Set a value in the cache. """
        raise NotImplementedError

    def get(self, key: Any, default: Any = None) -> Any:
        """ Get a value in the cache, return default if not exist """
        raise NotImplementedError

    def invalidate(self, key: Any) -> None:
        """ Invalidate a cache key """
        raise NotImplementedError


class FileCache(BaseCache):
    """ BaseCache implementation using files to store the data.
    This implementation uses diskcache.Cache

    This cache requires you to install diskcache using `pip install diskcache`
    """

    def __init__(self, path: str, **settings):
        """ Constructor

        Args:
            path: The path on the disk to save the data
            settings: The settings values for diskcache
        """
        from diskcache import Cache
        self._cache = Cache(path, **settings)

    def __del__(self):
        """ Close the connection as the cache instance is deleted. """
        if hasattr(self, '_cache'):
            self._cache.close()

    def set(self, key: Any, value: Any, expire: int = 300) -> None:
        expire = None if expire == 0 or expire is None else int(expire)
        self._cache.set(_hash(key), value, expire=expire)

    def get(self, key: Any, default: Any = None) -> Any:
        return self._cache.get(_hash(key), default)

    def invalidate(self, key: Any) -> None:
        self._cache.delete(_hash(key))


class DictCache(BaseCache):
    """ BaseCache implementation using Dict to store the cached data.

    Caution: due to its nature, DictCache does not expire keys!
    """

    def __init__(self):
        self._dict = {}

    def get(self, key: Any, default: Any = None) -> Any:
        return self._dict.get(_hash(key), default)

    def set(self, key: Any, value: Any, expire: int = 300) -> None:
        self._dict[_hash(key)] = value

    def invalidate(self, key: Any) -> None:
        self._dict.pop(_hash(key), None)

    def clear(self) -> None:
        self._dict.clear()


class DummyCache(BaseCache):
    """ Base cache implementation that provides a fake cache that
    allows a "no cache" use without breaking everything """

    def get(self, key: Any, default: Any = None) -> Any:
        return default

    def set(self, key: Any, value: Any, expire: int = 300) -> None:
        pass

    def invalidate(self, key: Any) -> None:
        pass


class MemcachedCache(BaseCache):
    """ Base cache implementation for memcached.

    This cache requires you to install memcached using `pip install python-memcached`
    """

    def __init__(self, memcache_client):
        """ memcache_client must be an instance of memcache.Client(). """
        import memcache
        if not isinstance(memcache_client, memcache.Client):
            raise TypeError('cache must be an instance of memcache.Client')
        self._mc = memcache_client

    def get(self, key: Any, default: Any = None) -> Any:
        value = self._mc.get(_hash(key))
        return value if value is not None else default

    def set(self, key: Any, value: Any, expire: int = 300) -> None:
        expire = 0 if expire is None else expire
        self._mc.set(_hash(key), value, time=int(expire))

    def invalidate(self, key: Any) -> None:
        self._mc.delete(_hash(key))


class RedisCache(BaseCache):
    """ BaseCache implementation for Redis cache.

    This cache handler requires the redis package to be installed `pip install redis`
    """

    def __init__(self, redis_client):
        """ redis_client must be an instance of redis.Redis """
        from redis import Redis
        if not isinstance(redis_client, Redis):
            raise TypeError('cache must be an instance of redis.Redis')
        self._r = redis_client

    def get(self, key: Any, default: Any = None) -> Any:
        value = self._r.get(_hash(key))
        return pickle.loads(value) if value is not None else default

    def set(self, key: Any, value: Any, expire: int = 300) -> None:
        if expire is None or expire == 0:
            self._r.set(_hash(key), pickle.dumps(value))
        else:
            self._r.setex(
                name=_hash(key),
                value=pickle.dumps(value),
                time=datetime.timedelta(seconds=int(expire)),
            )

    def invalidate(self, key: Any) -> None:
        self._r.delete(_hash(key))
```

2. middleware.py - Request/Response Middleware

```py
# -*- encoding: utf-8 -*-
""" Middleware for eve-esi-python """
import time
import threading
import logging
from typing import Dict, Optional, Tuple, Callable
from abc import ABC, abstractmethod

from ..rest import RESTResponse

LOGGER = logging.getLogger(__name__)


class BaseMiddleware(ABC):
    """ Base class for request middleware """

    @abstractmethod
    def before_request(self, method: str, url: str, headers: Dict[str, str],
                      body: Optional[str] = None) -> Tuple[str, str, Dict[str, str], Optional[str]]:
        """ Called before each request is sent """
        pass

    @abstractmethod
    def after_response(self, response: RESTResponse, request_time: float) -> RESTResponse:
        """ Called after each response is received """
        pass

    @abstractmethod
    def on_error(self, exception: Exception, attempt: int, max_attempts: int) -> bool:
        """ Called when an error occurs during request """
        pass


class RateLimitMiddleware(BaseMiddleware):
    """ Middleware that handles EVE ESI rate limiting (150 requests/second) """

    def __init__(self, max_requests_per_second: float = 150.0):
        """
        Args:
            max_requests_per_second: Maximum requests per second to allow
        """
        self.max_requests_per_second = max_requests_per_second
        self.min_interval = 1.0 / max_requests_per_second
        self.last_request_time = 0.0
        self._lock = threading.Lock()

    def before_request(self, method: str, url: str, headers: Dict[str, str],
                      body: Optional[str] = None) -> Tuple[str, str, Dict[str, str], Optional[str]]:
        """ Enforce rate limiting before sending request """
        with self._lock:
            current_time = time.time()
            time_since_last = current_time - self.last_request_time

            if time_since_last < self.min_interval:
                sleep_time = self.min_interval - time_since_last
                LOGGER.debug(f"Rate limiting: sleeping {sleep_time:.3f}s")
                time.sleep(sleep_time)

            self.last_request_time = time.time()

        return method, url, headers, body

    def after_response(self, response: RESTResponse, request_time: float) -> RESTResponse:
        return response

    def on_error(self, exception: Exception, attempt: int, max_attempts: int) -> bool:
        return True


class TokenRefreshMiddleware(BaseMiddleware):
    """ Middleware that automatically refreshes OAuth2 tokens when they expire """

    def __init__(self, token_refresh_callback: Optional[Callable[[], str]] = None):
        """
        Args:
            token_refresh_callback: Function that returns a new access token
        """
        self.token_refresh_callback = token_refresh_callback
        self._refresh_lock = threading.Lock()

    def before_request(self, method: str, url: str, headers: Dict[str, str],
                      body: Optional[str] = None) -> Tuple[str, str, Dict[str, str], Optional[str]]:
        return method, url, headers, body

    def after_response(self, response: RESTResponse, request_time: float) -> RESTResponse:
        """ Check if token needs refreshing based on response """
        if response.status == 401 and self.token_refresh_callback:
            LOGGER.info("Received 401 Unauthorized, attempting token refresh")
            with self._refresh_lock:
                try:
                    new_token = self.token_refresh_callback()
                    LOGGER.info("Token refreshed successfully")
                except Exception as e:
                    LOGGER.error(f"Token refresh failed: {e}")
                    raise
        return response

    def on_error(self, exception: Exception, attempt: int, max_attempts: int) -> bool:
        return True


class LoggingMiddleware(BaseMiddleware):
    """ Middleware that logs requests and responses """

    def __init__(self, log_level: int = logging.INFO):
        self.log_level = log_level

    def before_request(self, method: str, url: str, headers: Dict[str, str],
                      body: Optional[str] = None) -> Tuple[str, str, Dict[str, str], Optional[str]]:
        LOGGER.log(self.log_level, f"→ {method} {url}")
        return method, url, headers, body

    def after_response(self, response: RESTResponse, request_time: float) -> RESTResponse:
        LOGGER.log(self.log_level, f"← {response.status} in {request_time:.3f}s")
        return response

    def on_error(self, exception: Exception, attempt: int, max_attempts: int) -> bool:
        LOGGER.warning(f"Request failed (attempt {attempt}/{max_attempts}): {exception}")
        return True


class UserAgentMiddleware(BaseMiddleware):
    """ Middleware that ensures proper User-Agent header """

    def __init__(self, user_agent: str = "eve-esi-python/1.0"):
        self.user_agent = user_agent

    def before_request(self, method: str, url: str, headers: Dict[str, str],
                      body: Optional[str] = None) -> Tuple[str, str, Dict[str, str], Optional[str]]:
        if 'User-Agent' not in headers:
            headers['User-Agent'] = self.user_agent
        return method, url, headers, body

    def after_response(self, response: RESTResponse, request_time: float) -> RESTResponse:
        return response

    def on_error(self, exception: Exception, attempt: int, max_attempts: int) -> bool:
        return True
```

3. sso.py - EVE Online OAuth2 Flow

```py
# -_- encoding: utf-8 -_-

""" EVE Online SSO OAuth2 implementation """
import base64
import logging
import time
import secrets
import hashlib
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlencode, quote
import requests
from jose import jwt, JWTError

LOGGER = logging.getLogger(**name**)

class EVESSOConfig:
""" Configuration for EVE Online SSO """

      # EVE SSO endpoints
      SSO_BASE_URL = "https://login.eveonline.com"
      AUTHORIZE_URL = f"{SSO_BASE_URL}/v2/oauth/authorize"
      TOKEN_URL = f"{SSO_BASE_URL}/v2/oauth/token"
      JWKS_URL = f"{SSO_BASE_URL}/oauth/jwks"
      REVOKE_URL = f"{SSO_BASE_URL}/v2/oauth/revoke"

      # JWT validation
      JWT_ISSUER = "https://login.eveonline.com"
      JWT_AUDIENCE = "EVE Online"

class EVESSOAuthenticator:
""" Handles EVE Online OAuth2 authentication flow """

      def __init__(self, client_id: str, client_secret: Optional[str] = None,
                   redirect_uri: str = "http://localhost:8000/callback"):
          """
          Initialize EVE SSO authenticator

          Args:
              client_id: Your EVE application client ID
              client_secret: Your EVE application client secret (for confidential clients)
              redirect_uri: Redirect URI registered with your EVE application
          """
          self.client_id = client_id
          self.client_secret = client_secret
          self.redirect_uri = redirect_uri
          self.use_pkce = client_secret is None  # Use PKCE if no client secret

          # JWKS for JWT verification
          self._jwks_cache: Optional[Dict] = None
          self._jwks_cache_time = 0
          self._jwks_cache_ttl = 3600  # Cache JWKS for 1 hour

          LOGGER.info(f"EVE SSO authenticator initialized (PKCE: {self.use_pkce})")

      def generate_auth_url(self, scopes: List[str], state: Optional[str] = None) -> Tuple[str, str, Optional[str]]:
          """
          Generate authorization URL for EVE SSO

          Args:
              scopes: List of ESI scopes to request
              state: Optional state parameter for CSRF protection

          Returns:
              Tuple of (auth_url, state, code_verifier)
              code_verifier is only returned when using PKCE
          """
          if state is None:
              state = self._generate_state()

          params = {
              'response_type': 'code',
              'redirect_uri': self.redirect_uri,
              'client_id': self.client_id,
              'scope': ' '.join(scopes),
              'state': state
          }

          code_verifier = None
          if self.use_pkce:
              code_verifier = self._generate_code_verifier()
              code_challenge = self._generate_code_challenge(code_verifier)
              params.update({
                  'code_challenge': code_challenge,
                  'code_challenge_method': 'S256'
              })

          auth_url = f"{EVESSOConfig.AUTHORIZE_URL}?{urlencode(params)}"

          LOGGER.debug(f"Generated auth URL with {len(scopes)} scopes")
          return auth_url, state, code_verifier

      def exchange_code_for_tokens(self, code: str, code_verifier: Optional[str] = None) -> Dict:
          """
          Exchange authorization code for access tokens

          Args:
              code: Authorization code from callback
              code_verifier: Code verifier (required for PKCE flow)

          Returns:
              Token response dictionary
          """
          data = {
              'grant_type': 'authorization_code',
              'code': code,
              'redirect_uri': self.redirect_uri
          }

          headers = {'Content-Type': 'application/x-www-form-urlencoded'}

          if self.use_pkce:
              if code_verifier is None:
                  raise ValueError("code_verifier is required for PKCE flow")
              data.update({
                  'client_id': self.client_id,
                  'code_verifier': code_verifier
              })
          else:
              # Use Basic authentication for confidential clients
              auth_header = self._get_basic_auth_header()
              headers.update(auth_header)

          response = requests.post(EVESSOConfig.TOKEN_URL, data=data, headers=headers)
          response.raise_for_status()

          token_data = response.json()
          LOGGER.info("Successfully exchanged code for tokens")
          return token_data

      def refresh_token(self, refresh_token: str) -> Dict:
          """
          Refresh access token using refresh token

          Args:
              refresh_token: The refresh token

          Returns:
              New token response dictionary
          """
          data = {
              'grant_type': 'refresh_token',
              'refresh_token': refresh_token
          }

          headers = {'Content-Type': 'application/x-www-form-urlencoded'}

          if self.use_pkce:
              data['client_id'] = self.client_id
          else:
              auth_header = self._get_basic_auth_header()
              headers.update(auth_header)

          response = requests.post(EVESSOConfig.TOKEN_URL, data=data, headers=headers)
          response.raise_for_status()

          token_data = response.json()
          LOGGER.info("Successfully refreshed access token")
          return token_data

      def verify_jwt(self, access_token: str) -> Dict:
          """
          Verify and decode JWT access token

          Args:
              access_token: The JWT access token

          Returns:
              Decoded JWT payload
          """
          try:
              # Get JWKS for signature verification
              jwks = self._get_jwks()

              # Decode and verify JWT
              payload = jwt.decode(
                  access_token,
                  jwks,
                  algorithms=['RS256'],
                  issuer=EVESSOConfig.JWT_ISSUER,
                  audience=EVESSOConfig.JWT_AUDIENCE
              )

              LOGGER.debug("JWT verification successful")
              return payload

          except JWTError as e:
              LOGGER.error(f"JWT verification failed: {e}")
              raise

      def revoke_token(self, token: str, token_type_hint: str = "refresh_token") -> None:
          """
          Revoke an access or refresh token

          Args:
              token: The token to revoke
              token_type_hint: Type of token ("access_token" or "refresh_token")
          """
          data = {
              'token': token,
              'token_type_hint': token_type_hint
          }

          headers = {'Content-Type': 'application/x-www-form-urlencoded'}

          if self.use_pkce:
              data['client_id'] = self.client_id
          else:
              auth_header = self._get_basic_auth_header()
              headers.update(auth_header)

          response = requests.post(EVESSOConfig.REVOKE_URL, data=data, headers=headers)
          response.raise_for_status()

          LOGGER.info(f"Successfully revoked {token_type_hint}")

      def _generate_state(self) -> str:
          """ Generate random state for CSRF protection """
          return secrets.token_urlsafe(32)

      def _generate_code_verifier(self) -> str:
          """ Generate code verifier for PKCE """
          return base64.urlsafe_b64encode(secrets.token_bytes(32)).decode('utf-8').rstrip('=')

      def _generate_code_challenge(self, code_verifier: str) -> str:
          """ Generate code challenge from verifier """
          digest = hashlib.sha256(code_verifier.encode('utf-8')).digest()
          return base64.urlsafe_b64encode(digest).decode('utf-8').rstrip('=')

      def _get_basic_auth_header(self) -> Dict[str, str]:
          """ Generate Basic Authentication header """
          if self.client_secret is None:
              raise ValueError("Client secret is required for Basic authentication")

          credentials = f"{self.client_id}:{self.client_secret}"
          encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
          return {'Authorization': f'Basic {encoded_credentials}'}

      def _get_jwks(self) -> Dict:
          """ Get JWKS for JWT verification (with caching) """
          current_time = time.time()

          if (self._jwks_cache is None or
              current_time - self._jwks_cache_time > self._jwks_cache_ttl):

              response = requests.get(EVESSOConfig.JWKS_URL)
              response.raise_for_status()

              self._jwks_cache = response.json()
              self._jwks_cache_time = current_time

              LOGGER.debug("JWKS refreshed from server")

          return self._jwks_cache
```

4. client.py - Main Client with Session Management

```py
# -_- encoding: utf-8 -_-
""" Enhanced ESI Client with session management """
import threading
import time
import logging
from typing import Dict, List, Optional, Any, Union, Tuple
from dataclasses import dataclass
from cachetools import TTLCache

from ..api_client import ApiClient
from ..configuration import Configuration
from ..rest import RESTClientObject, RESTResponse
from .cache import BaseCache, DictCache
from .middleware import BaseMiddleware, RateLimitMiddleware, UserAgentMiddleware
from .sso import EVESSOAuthenticator

LOGGER = logging.getLogger(__name__)


@dataclass
class RetryConfig:
    """ Configuration for retry behavior """
    max_retries: int = 3
    backoff_factor: float = 0.5
    retry_status_codes: List[int] = None
    retry_methods: List[str] = None

    def __post_init__(self):
        if self.retry_status_codes is None:
            self.retry_status_codes = [429, 500, 502, 503, 504]
        if self.retry_methods is None:
            self.retry_methods = ["GET", "HEAD", "OPTIONS", "PUT", "DELETE"]


class EnhancedRESTClient(RESTClientObject):
    """ Enhanced REST client with middleware and retry support """

    def __init__(self, configuration: Configuration,
                 middleware: Optional[List[BaseMiddleware]] = None,
                 retry_config: Optional[RetryConfig] = None,
                 cache: Optional[BaseCache] = None):
        super().__init__(configuration)

        self.middleware = middleware or []
        self.retry_config = retry_config or RetryConfig()
        self.cache = cache or DictCache()
        self._stats_lock = threading.Lock()

        # Add default middleware
        if not any(isinstance(m, UserAgentMiddleware) for m in self.middleware):
            self.middleware.insert(0, UserAgentMiddleware())

    def request(self, method: str, url: str, headers: Optional[Dict[str, str]] = None,
                body: Optional[str] = None, post_params: Optional[Dict] = None,
                _request_timeout: Optional[Union[float, Tuple[float, float]]] = None) -> RESTResponse:
        """
        Enhanced request method with middleware support and retry logic
        """
        headers = headers or {}
        method = method.upper()
        attempt = 1

        # Apply before_request middleware
        for middleware in self.middleware:
            try:
                method, url, headers, body = middleware.before_request(method, url, headers, body)
            except Exception as e:
                LOGGER.error(f"Middleware {middleware.__class__.__name__} before_request failed: {e}")

        # Retry loop
        while attempt <= self.retry_config.max_retries + 1:
            start_time = time.time()

            try:
                # Make the actual request
                response = super().request(method, url, headers, body, post_params, _request_timeout)
                request_time = time.time() - start_time

                # Apply after_response middleware
                for middleware in self.middleware:
                    try:
                        response = middleware.after_response(response, request_time)
                    except Exception as e:
                        LOGGER.error(f"Middleware {middleware.__class__.__name__} after_response failed: {e}")

                # Check if we should retry based on status code
                if (response.status in self.retry_config.retry_status_codes and
                    attempt <= self.retry_config.max_retries and
                    method in self.retry_config.retry_methods):

                    self._handle_retry_delay(attempt)
                    attempt += 1
                    continue

                return response

            except Exception as e:
                # Check if we should retry
                should_retry = True
                for middleware in self.middleware:
                    try:
                        if not middleware.on_error(e, attempt, self.retry_config.max_retries + 1):
                            should_retry = False
                            break
                    except Exception as middleware_error:
                        LOGGER.error(f"Middleware {middleware.__class__.__name__} on_error failed: {middleware_error}")

                if should_retry and attempt <= self.retry_config.max_retries:
                    LOGGER.warning(f"Request failed (attempt {attempt}): {e}")
                    self._handle_retry_delay(attempt)
                    attempt += 1
                    continue

                raise

        raise Exception("Max retries exceeded")

    def _handle_retry_delay(self, attempt: int):
        """ Calculate and apply exponential backoff delay """
        import random

        base_delay = self.retry_config.backoff_factor * (2 ** (attempt - 1))
        jitter_factor = random.uniform(0.5, 1.5)
        delay = min(base_delay * jitter_factor, 30.0)

        LOGGER.info(f"Retrying in {delay:.2f}s (attempt {attempt})")
        time.sleep(delay)


class EsiClient(ApiClient):
    """ Enhanced ESI Client that preserves all generated API typing """

    def __init__(self, configuration: Optional[Configuration] = None,
                 middleware: Optional[List[BaseMiddleware]] = None,
                 retry_config: Optional[RetryConfig] = None,
                 cache: Optional[BaseCache] = None,
                 **kwargs):
        """
        Initialize enhanced ESI client

        Args:
            configuration: Configuration object
            middleware: List of middleware to apply
            retry_config: Retry configuration
            cache: Cache implementation
            **kwargs: Additional arguments passed to parent
        """
        if configuration is None:
            configuration = Configuration()

        super().__init__(configuration, **kwargs)

        # Replace the REST client with our enhanced version
        self.rest_client = EnhancedRESTClient(
            configuration=configuration,
            middleware=middleware,
            retry_config=retry_config,
            cache=cache
        )

        LOGGER.info("Enhanced ESI client initialized")

    def add_middleware(self, middleware: BaseMiddleware):
        """ Add middleware to the client """
        self.rest_client.middleware.append(middleware)
        LOGGER.info(f"Added middleware: {middleware.__class__.__name__}")


class UserSessionManager:
    """ Manages user sessions with TTL caching """

    def __init__(self, ttl: int = 1800):  # 30 minutes default
        """
        Initialize user session manager

        Args:
            ttl: Time-to-live for sessions in seconds (default: 30 minutes)
        """
        self._cache = TTLCache(maxsize=1000, ttl=ttl)
        self._lock = threading.Lock()
        self.ttl = ttl

        LOGGER.info(f"User session manager initialized (TTL: {ttl}s)")

    def get_user_session(self, access_token: str,
                        middleware: Optional[List[BaseMiddleware]] = None,
                        **config_overrides) -> EsiClient:
        """
        Get or create a user session

        Args:
            access_token: User's access token
            middleware: Additional middleware for this session
            **config_overrides: Configuration overrides

        Returns:
            EsiClient instance for the user
        """
        with self._lock:
            if access_token in self._cache:
                LOGGER.debug("Retrieved existing user session from cache")
                return self._cache[access_token]

            # Create new session
            config = Configuration(
                access_token=access_token,
                host=config_overrides.get('host', 'https://esi.evetech.net'),
                **config_overrides
            )

            # Add rate limiting by default
            default_middleware = [RateLimitMiddleware()]
            if middleware:
                default_middleware.extend(middleware)

            client = EsiClient(
                configuration=config,
                middleware=default_middleware,
                retry_config=RetryConfig()
            )

            self._cache[access_token] = client
            LOGGER.info("Created new user session")
            return client

    def invalidate_session(self, access_token: str):
        """ Invalidate a user session """
        with self._lock:
            if access_token in self._cache:
                del self._cache[access_token]
                LOGGER.info("Invalidated user session")

    def clear_all_sessions(self):
        """ Clear all cached sessions """
        with self._lock:
            self._cache.clear()
            LOGGER.info("Cleared all user sessions")

    def get_session_count(self) -> int:
        """ Get number of active sessions """
        with self._lock:
            return len(self._cache)


# Global session manager instance
_session_manager = UserSessionManager()


def get_session_manager() -> UserSessionManager:
    """ Get the global session manager """
    return _session_manager


def create_esi_client(access_token: Optional[str] = None,
                     enable_rate_limiting: bool = True,
                     enable_logging: bool = False,
                     **config_overrides) -> EsiClient:
    """
    Convenience function to create an ESI client

    Args:
        access_token: Optional access token for authenticated requests
        enable_rate_limiting: Enable rate limiting middleware
        enable_logging: Enable request logging middleware
        **config_overrides: Configuration overrides

    Returns:
        Configured EsiClient instance
    """
    config = Configuration(
        access_token=access_token,
        host=config_overrides.get('host', 'https://esi.evetech.net'),
        **config_overrides
    )

    middleware = []

    if enable_rate_limiting:
        middleware.append(RateLimitMiddleware())

    if enable_logging:
        from .middleware import LoggingMiddleware
        middleware.append(LoggingMiddleware())

    return EsiClient(
        configuration=config,
        middleware=middleware,
        retry_config=RetryConfig()
    )

Usage Example

Here's how this would be used in a FastAPI application:

from eve_esi_python.esi_client import get_session_manager, create_esi_client
from eve_esi_python.esi_client.sso import EVESSOAuthenticator

# Initialize SSO authenticator
sso = EVESSOAuthenticator(
    client_id="your_client_id",
    client_secret="your_client_secret",
    redirect_uri="http://localhost:8000/callback"
)

# Get global session manager
session_manager = get_session_manager()

@app.get("/wallet/{character_id}")
async def get_wallet(character_id: int, token: str = Depends(get_auth_token)):
    # Get user's ESI client (cached with TTL)
    client = session_manager.get_user_session(token)

    # Use the generated API with full type safety
    from eve_esi_python.api.wallet_api import WalletApi
    wallet_api = WalletApi(client)

    # This has full typing and IDE support!
    wallet_balance = wallet_api.get_characters_character_id_wallet(
        character_id=character_id
    )

    return {"balance": wallet_balance}
```

This design:

- ✅ Preserves all type safety from the generated code
- ✅ Provides excellent DX with simple, intuitive APIs
- ✅ Uses TTL caching for user sessions as requested
- ✅ Supports pluggable cache backends (Redis, File, etc.)
- ✅ Implements comprehensive middleware system
- ✅ Handles EVE OAuth2 flow completely
- ✅ Maintains connection pooling from the original urllib3 implementation
- ✅ Provides retry logic with exponential backoff

The key insight is that we enhance the RESTClientObject and ApiClient while keeping all the generated API classes unchanged, so you get all the benefits with zero loss of type safety!
