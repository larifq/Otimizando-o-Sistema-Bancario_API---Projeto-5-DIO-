from pydantic import BaseModel, Field, ConfigDict


class SchemaEnderecoOut(BaseModel):
    rua: str = Field(max_length=50)
    numero: str = Field(max_length=20)
    bairro: str = Field(max_length=50)
    cidade: str = Field(max_length=50)
    uf: str = Field(min_length=2, max_length=2)
    cep: str = Field(min_length=8, max_length=8)

    model_config = ConfigDict(from_attributes=True)