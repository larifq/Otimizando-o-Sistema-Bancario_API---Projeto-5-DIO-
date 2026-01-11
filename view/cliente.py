from pydantic import BaseModel, ConfigDict


class SchemaClienteOut(BaseModel):
    id: int
    id_endereco: int
    
    model_config = ConfigDict(from_attributes=True)
