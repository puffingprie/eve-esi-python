"""
eve-esi-python

ESI Scope Manager
"""

from typing import List, Set, Union
from pydantic import BaseModel, Field, field_validator

from eve_esi_python.esi.sso.constants import EsiScope


class EsiScopeManager(BaseModel):
    """Manager for type-safe EVE SSO OAuth scopes."""

    scopes: Set[EsiScope] = Field(default_factory=set)

    @field_validator("scopes", mode="before")
    @classmethod
    def validate_scopes(
        cls, value: Union[Set[EsiScope], List[Union[EsiScope, str]]]
    ) -> Set[EsiScope]:
        """Validate and convert input scopes (supports enums or strings)."""
        if isinstance(value, set):
            return value
        scopes_set = set()
        for scope in value:
            if isinstance(scope, EsiScope):
                scopes_set.add(scope)
            elif isinstance(scope, str):
                try:
                    scopes_set.add(EsiScope(scope))
                except ValueError:
                    raise ValueError(f"Invalid scope string: {scope}")
        return scopes_set

    def add_scope(self, scope: EsiScope) -> "EsiScopeManager":
        """Add a scope."""
        self.scopes.add(scope)
        return self

    def add_scopes(self, scopes: List[EsiScope]) -> "EsiScopeManager":
        """Add multiple scopes."""
        self.scopes.update(scopes)
        return self

    def remove_scope(self, scope: EsiScope) -> "EsiScopeManager":
        """Remove a scope."""
        self.scopes.discard(scope)
        return self

    def has_scope(self, scope: EsiScope) -> bool:
        """Check if a scope is present."""
        return scope in self.scopes

    def to_oauth_string(self) -> str:
        """Convert to space-separated string for OAuth (sorted for consistency)."""
        return " ".join(sorted(scope.value for scope in self.scopes))

    def get_scope_strings(self) -> List[str]:
        """Get sorted list of scope strings."""
        return sorted(scope.value for scope in self.scopes)

    def compare_scopes(self, jwt_scopes: Union[List[str], str, Set[EsiScope]]) -> bool:
        """Compare JWT scopes with current scopes to verify they match."""
        if isinstance(jwt_scopes, str):
            jwt_scope_strings = jwt_scopes.split()
        elif isinstance(jwt_scopes, list):
            jwt_scope_strings = jwt_scopes
        elif isinstance(jwt_scopes, set):
            jwt_scope_strings = [scope.value for scope in jwt_scopes]

        current_scope_strings = {scope.value for scope in self.scopes}
        jwt_scope_set = set(jwt_scope_strings)

        return current_scope_strings == jwt_scope_set
