from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Union

from app.database import SessionLocal
from app.models.persona import Persona
from app.models.empresa import Empresa
from app.schemas.response import PersonaResponse, EmpresaResponse
from app.security import verificar_api_key

router = APIRouter()

# Conexión a DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/consulta/{valor}",
    response_model=Union[PersonaResponse, EmpresaResponse]

)
def consultar(
    valor: str,
    db: Session = Depends(get_db),
    _: str = Depends(verificar_api_key)
):


    # Validar numérico
    if not valor.isdigit():
        raise HTTPException(status_code=400, detail="El valor debe ser numérico")

    # DNI
    if len(valor) == 8:
        persona = db.query(Persona).filter(Persona.dni == valor).first()
        if not persona:
            raise HTTPException(status_code=404, detail="DNI no encontrado")

        return PersonaResponse(
            tipo="DNI",
            dni=persona.dni,
            nombres=persona.nombres,
            apellido_paterno=persona.apellido_paterno,
            apellido_materno=persona.apellido_materno
        )

    # RUC
    elif len(valor) == 11:
        empresa = db.query(Empresa).filter(Empresa.ruc == valor).first()
        if not empresa:
            raise HTTPException(status_code=404, detail="RUC no encontrado")

        return EmpresaResponse(
            tipo="RUC",
            ruc=empresa.ruc,
            razon_social=empresa.razon_social,
            estado=empresa.estado,
            direccion=empresa.direccion
        )

    # Error
    else:
        raise HTTPException(
            status_code=400,
            detail="Debe tener 8 (DNI) o 11 (RUC) dígitos"
        )


