# CRUD de Personas con Flask

Trabajo Práctico - Aplicación de la receta de arquitectura en capas.

## Descripción

API REST simple para gestionar Personas (DNI + Nombre) usando Flask y una arquitectura limpia:

- **Model**: Contiene las reglas de negocio de consistencia del objeto (validaciones de formato).
- **Repository**: Encargado de la persistencia (en este TP se usa memoria).
- **Service**: Coordina reglas de negocio que requieren el repositorio (ej: unicidad de DNI).
- **API (endpoints)**: Capa de presentación / controlador HTTP.

## Estructura del proyecto

```
.
├── models/
│   └── persona.py              # Clase Persona + validaciones de dominio
├── repositories/
│   └── persona_repository.py   # Persistencia (en memoria)
├── services/
│   └── persona_service.py      # Reglas de negocio de aplicación
├── api.py                      # Endpoints Flask
├── requirements.txt
└── README.md
```

### Cómo me gusta trabajar (contexto para la IA / futuros prompts)

- El **modelo** nunca conoce el repositorio ni el servicio.
- Las validaciones de formato y consistencia del objeto viven en el **modelo**.
- Las reglas de negocio que necesitan consultar el repositorio (unicidad, etc.) viven en el **servicio**.
- El repositorio solo se ocupa de guardar / buscar / eliminar.
- Los endpoints solo reciben HTTP, llaman al servicio y devuelven JSON + códigos de estado.
- Preferimos mensajes de error claros y códigos HTTP correctos (400, 404, 201, etc.).

## Requisitos

- Python 3.10+
- Flask

```bash
pip install -r requirements.txt
```

## Cómo ejecutar

```bash
python api.py
```

La API queda disponible en: `http://localhost:5000`

## Endpoints implementados (solo GET y POST según consignas)

| Método | Ruta              | Descripción                     |
|--------|-------------------|---------------------------------|
| GET    | `/personas`       | Lista todas las personas        |
| GET    | `/personas/<dni>` | Obtiene una persona por DNI     |
| POST   | `/personas`       | Crea una nueva persona          |

### Ejemplo de body para POST

```json
{
  "dni": "12345678",
  "nombre": "Juan perez"
}
```

### Validaciones

- **DNI**: obligatorio, solo números, no puede estar duplicado.
- **Nombre**:
  - Obligatorio
  - Máximo 30 caracteres
  - Debe comenzar con mayúscula
  - El resto de las letras deben estar en minúscula
  - Solo letras y espacios

## Cómo probar con Thunder Client (VS Code)

1. Instalar la extensión **Thunder Client**.
2. Crear una nueva request:

**Crear persona (POST)**
- Method: `POST`
- URL: `http://localhost:5000/personas`
- Body → JSON:
  ```json
  {
    "dni": "30123456",
    "nombre": "Maria lopez"
  }
  ```

**Listar todas (GET)**
- Method: `GET`
- URL: `http://localhost:5000/personas`

**Obtener una (GET)**
- Method: `GET`
- URL: `http://localhost:5000/personas/30123456`

## Notas

- La persistencia es en memoria: al reiniciar el servidor se pierden los datos.
- No se implementaron PUT ni DELETE (según consignas del TP).
```