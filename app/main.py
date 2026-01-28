from dotenv import load_dotenv
import os

# 🔐 Cargar variables de entorno PRIMERO
load_dotenv()

from fastapi import FastAPI
from app.database import Base, engine
from app.routes.consulta import router as consulta_router

app = FastAPI(title="API Consulta DNI / RUC")

Base.metadata.create_all(bind=engine)

app.include_router(consulta_router)

@app.get("/")
def root():
    return {"mensaje": "API DNI/RUC funcionando"}


