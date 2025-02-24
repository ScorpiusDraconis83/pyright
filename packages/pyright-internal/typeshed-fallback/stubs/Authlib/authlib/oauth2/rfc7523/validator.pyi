from _typeshed import Incomplete

from authlib.jose import JWTClaims
from authlib.oauth2.rfc6749 import TokenMixin
from authlib.oauth2.rfc6750 import BearerTokenValidator

logger: Incomplete

class JWTBearerToken(TokenMixin, JWTClaims):
    def check_client(self, client): ...
    def get_scope(self): ...
    def get_expires_in(self): ...
    def is_expired(self): ...
    def is_revoked(self): ...

class JWTBearerTokenValidator(BearerTokenValidator):
    TOKEN_TYPE: str
    token_cls = JWTBearerToken
    public_key: Incomplete
    claims_options: Incomplete
    def __init__(
        self, public_key, issuer: Incomplete | None = None, realm: Incomplete | None = None, **extra_attributes
    ) -> None: ...
    def authenticate_token(self, token_string): ...
