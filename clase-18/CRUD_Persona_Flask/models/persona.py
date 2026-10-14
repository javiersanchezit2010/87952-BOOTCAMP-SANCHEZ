class Persona:
    def __init__(self, dni: str, nombre: str):
        self._validar_dni(dni)
        self._validar_nombre(nombre)
        self.dni = dni
        self.nombre = nombre

    def _validar_dni(self, dni: str) -> None:
        if not dni or not isinstance(dni, str):
            raise ValueError("El DNI es obligatorio y debe ser un string")
        if not dni.strip():
            raise ValueError("El DNI no puede estar vacío")
        # Opcional: validar formato numérico básico
        if not dni.isdigit():
            raise ValueError("El DNI debe contener solo números")

    def _validar_nombre(self, nombre: str) -> None:
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre es obligatorio y debe ser un string")
        nombre = nombre.strip()
        if len(nombre) == 0:
            raise ValueError("El nombre no puede estar vacío")
        if len(nombre) > 30:
            raise ValueError("El nombre no puede tener más de 30 caracteres")
        # Debe empezar con mayúscula y el resto minúsculas
        if not nombre[0].isupper():
            raise ValueError("El nombre debe comenzar con mayúscula")
        if len(nombre) > 1 and not nombre[1:].islower():
            raise ValueError("El nombre debe tener el resto de letras en minúscula")
        # Solo letras y espacios permitidos (simple)
        if not all(c.isalpha() or c.isspace() for c in nombre):
            raise ValueError("El nombre solo puede contener letras y espacios")

    def to_dict(self) -> dict:
        return {
            "dni": self.dni,
            "nombre": self.nombre
        }

    def __repr__(self) -> str:
        return f"Persona(dni={self.dni}, nombre={self.nombre})"
