from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class SchemaPessoaFisicaOut(BaseModel):

    cpf: str = Field(min_length=11, max_length=11)
    nome: str = Field(max_length=20)
    data_nascimento: date
