from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal
from schemas.login import SchemaLogin
class SchemaConta(BaseModel):
    saldo: Decimal
    agencia: str = Field(default="01")
    id_cliente: int = Field(gt=0)
    login: SchemaLogin
    
class SchemaContaUpdate(BaseModel):
    saldo: Optional[Decimal] = Field(None)
    agencia: Optional[str] = Field(None)
    id_cliente: Optional[int] = Field(None, gt=0)
    
