from models.persona import Persona


class PersonaRepository:
    """In-memory persistence for personas."""

    def __init__(self):
        self._personas: dict[str, Persona] = {}

    def guardar(self, persona: Persona) -> None:
        self._personas[persona.dni] = persona

    def obtener_todos(self) -> list[Persona]:
        return list(self._personas.values())

    def obtener_por_dni(self, dni: str) -> Persona | None:
        return self._personas.get(dni)

    def existe_dni(self, dni: str) -> bool:
        return dni in self._personas

    def limpiar(self) -> None:
        """Remove all records; useful for resetting the in-memory store."""
        self._personas.clear()
