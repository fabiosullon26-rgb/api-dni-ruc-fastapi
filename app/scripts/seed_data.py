from app.database import SessionLocal
from app.models.persona import Persona
from app.models.empresa import Empresa

def insertar_datos():
    db = SessionLocal()

    # ---------------- PERSONAS (DNI) ----------------
    personas = [
        Persona(dni="12345678", nombres="Juan", apellido_paterno="Perez", apellido_materno="Gomez"),
        Persona(dni="87654321", nombres="Maria", apellido_paterno="Lopez", apellido_materno="Diaz"),
        Persona(dni="11223344", nombres="Carlos", apellido_paterno="Ramirez", apellido_materno="Torres"),
        Persona(dni="44332211", nombres="Ana", apellido_paterno="Sanchez", apellido_materno="Rojas"),
        Persona(dni="55667788", nombres="Luis", apellido_paterno="Vargas", apellido_materno="Mendoza"),
        Persona(dni="99887766", nombres="Carmen", apellido_paterno="Flores", apellido_materno="Castro"),
        Persona(dni="33445566", nombres="Pedro", apellido_paterno="Gutierrez", apellido_materno="Silva"),
        Persona(dni="66778899", nombres="Lucia", apellido_paterno="Navarro", apellido_materno="Paredes"),
        Persona(dni="22113344", nombres="Miguel", apellido_paterno="Ortega", apellido_materno="Salinas"),
        Persona(dni="88990011", nombres="Rosa", apellido_paterno="Quispe", apellido_materno="Huaman"),
    ]

    # ---------------- EMPRESAS (RUC) ----------------
    empresas = [
        Empresa(ruc="20123456789", razon_social="Empresa Uno SAC", estado="ACTIVO", direccion="Av. Lima 123"),
        Empresa(ruc="20987654321", razon_social="Comercial Dos SRL", estado="ACTIVO", direccion="Jr. Arequipa 456"),
        Empresa(ruc="20445566778", razon_social="Servicios Tres SAC", estado="ACTIVO", direccion="Av. Peru 789"),
        Empresa(ruc="20556677889", razon_social="Industria Cuatro SA", estado="INACTIVO", direccion="Av. Brasil 101"),
        Empresa(ruc="20667788990", razon_social="Negocios Cinco SAC", estado="ACTIVO", direccion="Jr. Cusco 202"),
        Empresa(ruc="20778899001", razon_social="Importaciones Seis SRL", estado="ACTIVO", direccion="Av. Grau 303"),
        Empresa(ruc="20889900112", razon_social="Exportadora Siete SAC", estado="ACTIVO", direccion="Av. Tacna 404"),
        Empresa(ruc="20990011223", razon_social="Logistica Ocho SAC", estado="INACTIVO", direccion="Jr. Moquegua 505"),
        Empresa(ruc="20112233445", razon_social="Consultora Nueve SRL", estado="ACTIVO", direccion="Av. La Marina 606"),
        Empresa(ruc="20223344556", razon_social="Tecnologia Diez SAC", estado="ACTIVO", direccion="Av. Universitaria 707"),
    ]

    # Insertar datos
    db.add_all(personas)
    db.add_all(empresas)
    db.commit()
    db.close()

    print("✅ Datos insertados correctamente")

if __name__ == "__main__":
    insertar_datos()
