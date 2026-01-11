from pydantic import BaseModel

class SchemaJWT(BaseModel):
    iss: str
    sub: int
    aud: str
    exp: float
    jti: str

class SchemaToken(BaseModel):
    token_acesso: str



