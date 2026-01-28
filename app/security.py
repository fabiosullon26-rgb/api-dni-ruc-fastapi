from fastapi import Header, HTTPException
import os

API_KEY = os.getenv("API_KEY")

def verificar_api_key(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="API Key requerida")

    esquema, _, token = authorization.partition(" ")

    if esquema.lower() != "bearer" or token != API_KEY:
        raise HTTPException(status_code=401, detail="API Key inválida")