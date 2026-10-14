from models.persona import Persona
from typing import List, Optional


class PersonaRepository:
    """
    Repositorio en memoria para Personas.
    En un proyecto real se usaría una base de datos (SQLAlchemy, etc.).
    """

    def __init__(self):
        self._personas: List[Persona] = []

    def guardar(self, persona: Persona) -> Persona:
        """Guarda una nueva persona. Asume que ya se validó unicidad del DNI."""
        self._personas.append(persona)
        return persona

    def obtener_todas(self) -> List[Persona]:
        """Retorna todas las personas."""
        return list(self._personas)

    def obtener_por_dni(self, dni: str) -> Optional[Persona]:
        """Busca una persona por DNI. Retorna None si no existe."""
        for persona in self._personas:
            if persona.dni == dni:
                return persona
        return None

    def existe_dni(self, dni: str) -> bool:
        """Verifica si ya existe un DNI."""
        return self.obtener_por_dni(dni) is not None

    def eliminar(self, dni: str) -> bool:
        """Elimina una persona por DNI. Retorna True si se eliminó."""
        persona = self.obtener_por_dni(dni)
        if persona:
            self._personas.remove(persona)
            return True
        return False

    def actualizar(self, dni: str, nueva_persona: Persona) -> Optional[Persona]:
        """Actualiza una persona existente. Retorna la actualizada o None."""
        for i, persona in enumerate(self._personas):
            if persona.dni == dni:
                self._personas[i] = nueva_persona
                return nueva_persona
        return None
