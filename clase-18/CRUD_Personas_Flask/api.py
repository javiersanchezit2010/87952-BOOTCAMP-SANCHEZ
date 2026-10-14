from flask import Flask, jsonify, request

from repositories.persona_repository import PersonaRepository
from services.persona_service import DNIRepetidoError, PersonaService


app = Flask(__name__)
repository = PersonaRepository()
persona_service = PersonaService(repository)


@app.get("/personas")
def listar_personas():
    personas = persona_service.listar_personas()
    return jsonify([persona.to_dict() for persona in personas]), 200


@app.get("/personas/<string:dni>")
def obtener_persona(dni: str):
    persona = persona_service.buscar_por_dni(dni)
    if persona is None:
        return jsonify({"error": "No se encontró una persona con ese DNI."}), 404
    return jsonify(persona.to_dict()), 200


@app.post("/personas")
def crear_persona():
    datos = request.get_json(silent=True)
    if not isinstance(datos, dict):
        return jsonify({"error": "El cuerpo debe ser un objeto JSON."}), 400

    try:
        persona = persona_service.crear_persona(
            dni=datos.get("dni"),
            nombre=datos.get("nombre"),
        )
    except DNIRepetidoError as error:
        return jsonify({"error": str(error)}), 409
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    return jsonify(persona.to_dict()), 201


if __name__ == "__main__":
    app.run(debug=True)
