from pydantic import BaseModel, Field
from typing import Optional

class SchemaLogin(BaseModel):
    id: Optional[int] = Field(None)
    senha: str

class SchemaLoginResponse(BaseModel):
    id: int
    senha: str
