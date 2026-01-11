from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class SchemaHistoricoOut(BaseModel):
    valor: float
    tipo_transacao: str = Field(max_length=8)
    data_transacao: datetime

    model_config = ConfigDict(from_attributes=True)


class SchemaDepositoOut(BaseModel):
    valor: float
    data_transacao: datetime
    saldo_atual: Optional[float] = Field(default=None)
    model_config = ConfigDict(from_attributes=True)


class SchemaSaqueOut(BaseModel):
    valor: float
    data_transacao: datetime
    saldo_atual: Optional[float] = Field(default=None)

    model_config = ConfigDict(from_attributes=True)
