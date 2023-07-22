import uuid
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Es una función que se utiliza para definir una clase base que actúa como una base 
#    para todas las clases de modelo (tablas) que definirás en tu aplicación
# Cuando defines tus modelos (tablas) utilizando clases, debes hacer que hereden de esta clase base.
Base = declarative_base()

class tasks(Base):
    __tablename__ = "tareas"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    userId = Column(UUID(as_uuid=True))
    tarea = Column(String(255))
    fecha = Column(Date, default=datetime.date(datetime.now()))  # Aquí se establece la fecha actual
    idState = Column(Integer)


# {
#     "userID" : "idUsuario",
#     "tarea" : "",
#     "idState" : 1
# }
