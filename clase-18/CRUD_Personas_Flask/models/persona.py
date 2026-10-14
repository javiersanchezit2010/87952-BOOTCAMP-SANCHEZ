import re


class Persona:
    """Persona with its lifecycle invariants enforced at construction."""

    _NOMBRE_PATTERN = re.compile(r"^[A-ZÁÉÍÓÚÜÑ][a-záéíóúüñ ]*$")
    _MAX_NOMBRE_LENGTH = 30

    def __init__(self, dni: str, nombre: str):
        if not isinstance(dni, str) or not dni.strip():
            raise ValueError("El DNI es obligatorio y debe ser texto.")
        if dni != dni.strip():
            raise ValueError("El DNI no puede tener espacios al inicio o al final.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre es obligatorio y debe ser texto.")
        if nombre != nombre.strip():
            raise ValueError("El nombre no puede tener espacios al inicio o al final.")
        if len(nombre) > self._MAX_NOMBRE_LENGTH:
            raise ValueError("El nombre no puede tener más de 30 caracteres.")
        if not self._NOMBRE_PATTERN.fullmatch(nombre):
            raise ValueError(
                "El nombre debe comenzar con mayúscula y continuar con minúsculas."
            )

        self.dni = dni
        self.nombre = nombre

    def to_dict(self) -> dict[str, str]:
        return {"dni": self.dni, "nombre": self.nombre}
