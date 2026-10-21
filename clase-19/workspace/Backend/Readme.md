
# Estructura del proyecto

/
├── api.py
├── models/
│   └── alumno.py
└── repositories/
    └── alumno_repository.py
├── services/
│   └── alumno_service.py

## Personas

- `PUT /persona/<dni>`: actualiza el nombre de la persona identificada por DNI.
  El body debe ser JSON con la forma `{"nombre": "NuevoNombre"}`.
- `DELETE /persona/<dni>`: elimina la persona identificada por DNI.

Ambos endpoints responden con HTTP 400 si no existe una persona con ese DNI.
