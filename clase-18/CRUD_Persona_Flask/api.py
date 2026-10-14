from flask import Flask, request, jsonify
from repositories.persona_repository import PersonaRepository
from services.persona_service import PersonaService

app = Flask(__name__)

# Instanciamos el repositorio y el servicio (singleton simple para el TP)
persona_repo = PersonaRepository()
persona_service = PersonaService(persona_repo)


@app.route("/personas", methods=["GET"])
def obtener_todas_personas():
    """GET /personas - Lista todas las personas"""
    personas = persona_service.obtener_todas()
    return jsonify([p.to_dict() for p in personas]), 200


@app.route("/personas/<dni>", methods=["GET"])
def obtener_persona(dni: str):
    """GET /personas/<dni> - Obtiene una persona por DNI"""
    persona = persona_service.obtener_por_dni(dni)
    if persona is None:
        return jsonify({"error": f"No se encontró persona con DNI {dni}"}), 404
    return jsonify(persona.to_dict()), 200


@app.route("/personas", methods=["POST"])
def crear_persona():
    """POST /personas - Crea una nueva persona"""
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Se requiere un cuerpo JSON"}), 400

    dni = data.get("dni")
    nombre = data.get("nombre")

    if dni is None or nombre is None:
        return jsonify({"error": "Los campos 'dni' y 'nombre' son obligatorios"}), 400

    try:
        persona = persona_service.crear_persona(str(dni), str(nombre))
        return jsonify(persona.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    # Modo desarrollo. En producción usar un servidor WSGI.
    app.run(debug=True, host="0.0.0.0", port=5000)
