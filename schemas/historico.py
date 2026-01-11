from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal, Optional
from decimal import Decimal

class SchemaHistorico(BaseModel):
    valor:  Optional[Decimal] = Field(gt=0)
    tipo_transacao: Optional[Literal["Saque", "Deposito"]]
    tipo_conta: Optional[Literal["Conta Corrente", "Conta Poupança"]]
    data_transacao: Optional[datetime] = Field(default=datetime.now())
    id_conta: Optional[int] = Field(gt=0)

class SchemaTransacao(BaseModel):
    valor:  Optional[Decimal] = Field(gt=0)