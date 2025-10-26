from typing import Optional, List
from pydantic import BaseModel as SCBaseModel, HttpUrl,ConfigDict


class ArtigoSchema(SCBaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: HttpUrl
    usuario_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)