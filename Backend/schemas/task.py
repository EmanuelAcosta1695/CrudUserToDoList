import uuid
from pydantic import BaseModel
from datetime import date


class createTask(BaseModel):
    usuario_id : uuid.UUID
    tarea: str
    id_estado: int


class responseTask(BaseModel):
    id: uuid.UUID
    usuario_id : uuid.UUID
    tarea: str
    fecha: date
    id_estado: int


class updateTask(BaseModel):
    usuario_id : uuid.UUID
    tarea: str
    id_estado: int