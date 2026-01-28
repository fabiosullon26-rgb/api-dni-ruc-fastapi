from sqlalchemy import Column, Integer, String
from app.database import Base

class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String(8), unique=True, index=True)
    nombres = Column(String)
    apellido_paterno = Column(String)
    apellido_materno = Column(String)
