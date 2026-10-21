from datetime import date

from flask import Flask, jsonify, request
from flask_cors import CORS

from models.alumno import Alumno
from services.alumno_service import AlumnoService


app = Flask(__name__)
CORS(app)
servicio = AlumnoService()


@app.get("/alumnos")
def obtener_alumnos():
    alumnos = servicio.obtener_alumnos()

    return jsonify([
        {
            "legajo": alumno.legajo,
            "nombre": alumno.nombre,
            "apellido": alumno.apellido,
            "fechaDeNacimiento": alumno.fecha_de_nacimiento.isoformat()
        }
        for alumno in alumnos
    ])


@app.get("/alumnos/<int:legajo>")
def obtener_alumno(legajo):
    alumno = servicio.obtener_alumno_por_legajo(legajo)

    if alumno is None:
        return jsonify({
            "error": "Alumno no encontrado"
        }), 404

    return jsonify({
        "legajo": alumno.legajo,
        "nombre": alumno.nombre,
        "apellido": alumno.apellido,
        "fechaDeNacimiento": alumno.fecha_de_nacimiento.isoformat()
    })


@app.post("/alumnos")
def agregar_alumno():
    datos = request.get_json()

    alumno = Alumno(
        datos["legajo"],
        datos["nombre"],
        datos["apellido"],
        date.fromisoformat(datos["fechaDeNacimiento"])
    )

    try:
        servicio.agregar_alumno(alumno)
    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 409

    return jsonify({
        "legajo": alumno.legajo,
        "nombre": alumno.nombre,
        "apellido": alumno.apellido,
        "fechaDeNacimiento": alumno.fecha_de_nacimiento.isoformat()
    }), 201


@app.delete("/persona/<int:dni>")
def eliminar_persona(dni):
    try:
        servicio.eliminar_alumno(dni)
    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 400

    return "", 204


@app.put("/persona/<int:dni>")
def actualizar_persona(dni):
    datos = request.get_json()
    if not isinstance(datos, dict) or not isinstance(datos.get("nombre"), str):
        return jsonify({
            "error": "El campo nombre es obligatorio."
        }), 400

    try:
        alumno = servicio.actualizar_nombre(dni, datos["nombre"])
    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 400

    return jsonify({
        "legajo": alumno.legajo,
        "nombre": alumno.nombre,
        "apellido": alumno.apellido,
        "fechaDeNacimiento": alumno.fecha_de_nacimiento.isoformat()
    })


if __name__ == "__main__":
    app.run(debug=True)