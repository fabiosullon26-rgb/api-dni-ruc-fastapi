from sqlalchemy import Column, Integer, String
from app.database import Base

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    ruc = Column(String(11), unique=True, index=True)
    razon_social = Column(String)
    estado = Column(String)
    direccion = Column(String)
