from datetime import date

from flask import Flask, jsonify, request

from models.alumno import Alumno
from repositories.alumno_repository import RepositorioAlumnos


app = Flask(__name__)

repositorio = RepositorioAlumnos()


@app.get("/alumnos")
def obtener_alumnos():
    alumnos = repositorio.obtener_todos()

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
    alumno = repositorio.obtener_por_legajo(legajo)

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

    repositorio.guardar(alumno)

    return jsonify({
        "legajo": alumno.legajo,
        "nombre": alumno.nombre,
        "apellido": alumno.apellido,
        "fechaDeNacimiento": alumno.fecha_de_nacimiento.isoformat()
    }), 201


if __name__ == "__main__":
    app.run(debug=True)