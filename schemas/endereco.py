from pydantic import BaseModel, Field
from typing import Optional

class SchemaEndereco(BaseModel):
    
    rua: str = Field(max_length=50)
    numero: str = Field(max_length=20)
    bairro: str = Field(max_length=50)
    cidade: str = Field(max_length=50)
    uf: str = Field(min_length=2, max_length=2)
    cep: str = Field(min_length=8, max_length=8)


class SchemaEnderecoUpdate(BaseModel):

    rua: Optional[str] = Field(None, max_length=50)
    numero: Optional[str] = Field(None, max_length=20)
    bairro: Optional[str] = Field(None, max_length=50)
    cidade: str = Field(None, max_length=50)
    uf: Optional[str] = Field(None, min_length=2, max_length=2)
    cep: Optional[str] = Field(None, min_length=8, max_length=8)