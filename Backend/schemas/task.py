import uuid
from pydantic import BaseModel
from datetime import date

class createTask(BaseModel):
    userId : uuid.UUID
    tarea: str
    idState: int


class responseTask(BaseModel):
    id: uuid.UUID
    userId : uuid.UUID
    tarea: str
    fecha: date
    idState: int


class updateTask(BaseModel):
    userId : uuid.UUID
    tarea: str
    idState: int