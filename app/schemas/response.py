from pydantic import BaseModel

# Respuesta para DNI
class PersonaResponse(BaseModel):
    tipo: str
    dni: str
    nombres: str
    apellido_paterno: str
    apellido_materno: str


# Respuesta para RUC
class EmpresaResponse(BaseModel):
    tipo: str
    ruc: str
    razon_social: str
    estado: str
    direccion: str
