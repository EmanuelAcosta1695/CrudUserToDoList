import uuid
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class users(Base):
    __tablename__ = "usuarios"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(255))
    edad = Column(Integer)  
    correo = Column(String(255))

# UUID(as_uuid=True), primary_key=True, default=uuid.uuid4