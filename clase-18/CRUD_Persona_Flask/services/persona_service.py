from models.persona import Persona
from repositories.persona_repository import PersonaRepository
from typing import List, Optional


class PersonaService:
    """
    Servicio que coordina reglas de negocio que involucran
    al modelo y al repositorio.
    """

    def __init__(self, repository: PersonaRepository):
        self.repository = repository

    def crear_persona(self, dni: str, nombre: str) -> Persona:
        """
        Crea una nueva Persona aplicando reglas de negocio:
        - El DNI no puede estar duplicado
        - El modelo valida formato de nombre y DNI
        """
        # Regla de negocio: no DNI duplicado
        if self.repository.existe_dni(dni):
            raise ValueError(f"Ya existe una persona con el DNI {dni}")

        # El modelo aplica sus propias validaciones (nombre, formato, etc.)
        persona = Persona(dni=dni, nombre=nombre)
        return self.repository.guardar(persona)

    def obtener_todas(self) -> List[Persona]:
        return self.repository.obtener_todas()

    def obtener_por_dni(self, dni: str) -> Optional[Persona]:
        return self.repository.obtener_por_dni(dni)
