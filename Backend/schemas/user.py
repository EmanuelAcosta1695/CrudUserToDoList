import uuid
from pydantic import BaseModel


class createUser(BaseModel):
    nombre: str
    edad: int
    correo: str


class responseUser(BaseModel):
    id: uuid.UUID
    nombre: str
    edad: int
    correo: str


class updateUser(BaseModel):
    nombre: str
    edad: int
    correo: str