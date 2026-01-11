from pydantic import BaseModel, Field
from typing import Optional

from schemas.conta import SchemaConta

class SchemaContaCorrente(BaseModel):
    limite:float = Field(gt=0)
    limite_saque: int = Field(ge=0, default=0)
    conta: SchemaConta

class SchemaContaCorrenteUpdate(BaseModel):
    limite: Optional[float] = Field(None, gt=0)
    limite_saque: Optional[int] = Field(None, ge=0)
    