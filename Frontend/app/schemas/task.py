import uuid
from pydantic import BaseModel

# Colocar un dato como opcional
from typing import Optional

class optionalArgGetTasks(BaseModel):
    filtro: Optional[str]


class optionalArgUserTasks(BaseModel):
    name: Optional[str]
    correo: Optional[int]
    idUser: Optional[uuid.UUID]



class optionalArgUpdate(BaseModel):
    id: uuid.UUID
    estado: Optional[str]
    pagina: Optional[str]



class optionalArgDelete(BaseModel):
    id: uuid.UUID
    pagina: Optional[str]