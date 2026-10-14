from models.persona import Persona
from repositories.persona_repository import PersonaRepository


class DNIRepetidoError(Exception):
    """Raised when a persona is created with an already registered DNI."""


class PersonaService:
    def __init__(self, repository: PersonaRepository):
        self._repository = repository

    def listar_personas(self) -> list[Persona]:
        return self._repository.obtener_todos()

    def buscar_por_dni(self, dni: str) -> Persona | None:
        return self._repository.obtener_por_dni(dni)

    def crear_persona(self, dni: str, nombre: str) -> Persona:
        if self._repository.existe_dni(dni):
            raise DNIRepetidoError("Ya existe una persona con ese DNI.")

        persona = Persona(dni, nombre)
        self._repository.guardar(persona)
        return persona
