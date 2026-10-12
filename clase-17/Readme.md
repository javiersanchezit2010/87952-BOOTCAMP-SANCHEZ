# Clase 17 - 5 de Octubre del 2026

# Repaso

* Arquitectura de SW
  * Division en Capas
    * Presentacion
    * Modelo
    * Repositorio / Persistencia
  * Reglas de Negocio
    * Ejemplo
      * Calculo
      * Decision
      * Restriciones / Validadioncs
      * Proceso
      * Accion
    * Si tien que ver con un objeto o grupo de objetos relacionados -> Mejor en la capa de modelo
    * Si necesitas una vista general de todos los objetos -> Necesito la capa de servicios
* Python
  * Ejempleficamos con el CRUD con FlasK
    * CRUD de Alumno
    * APIs

---

# Novedades

* Modelo para tomar decisiones
 * JEV
  * https://jev-ai.org/

# Arquitectura de SW

## Restricciones

* Evitar acceder al Repositorio desde el modelo. Para eso esta la capa de servicios

## Capa de Servicios

> Es una capa adicional que se coloca entre la presentacion y el modelo. Orquesta y coordina las operaciones del negocio que necesitan coordinar entre varias clases del modelo distintas.

* Version 1
```python
from models.alumno import Alumno
from repositories.alumno_repository import AlumnoRepository


class AlumnoService:
    def __init__(self):
        self.repo = AlumnoRepository() 

    def agregar_alumno(self, alumno: Alumno):
        self.repo.agregar_alumno(alumno)

    def obtener_alumnos(self):
        return self.repo.obtener_alumnos()

    def obtener_alumno_por_id(self, alumno_id: int):
        return self.repo.obtener_alumno_por_id(alumno_id)
```

* Ahor vamos a refactorizar la API para que utilice el servicio y no acceda al repositorio directamente

```python
from datetime import date

from flask import Flask, jsonify, request

from models.alumno import Alumno
from services.alumno_service import AlumnoService


app = Flask(__name__)

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

    servicio.agregar_alumno(alumno)

    return jsonify({
        "legajo": alumno.legajo,
        "nombre": alumno.nombre,
        "apellido": alumno.apellido,
        "fechaDeNacimiento": alumno.fecha_de_nacimiento.isoformat()
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
```

> [!NOTE]
> Le saque las variable global serivicio y lo instancie en cada metodo/endpoint. Para no tener varables globales. 
> Evitar el uso de variables globales es una buena practica

* HAsta ahora la capa de servicios quedo bastante plana. Es un pasamano. Vamos a agregarle alguna logica de negocios
 * Si hay una validacion que tiene que ver con el alumno, por ejemplo el largo de su nombre, esa validacion la podesmos poner en el modelo
 * Ahora si necesitamos ademas ver si existe otro alumno con un determinado legajo y consultar para eso el repsoitorio, esta clase de cosas van en la capa de servicio

```
User: Quiero validar que no haya dos alumnos cn el mismo legajo. Quiero validarlo al agregar el alumno. Donde pongo esa validacion?

Poné la validación en `agregar_alumno` de `alumno_service.py`: el servicio coordina la regla de negocio y el repositorio ya ofrece `obtener_por_legajo`.

def agregar_alumno(self, alumno: Alumno) -> None:
    if self.repo.obtener_por_legajo(alumno.legajo) is not None:
        raise ValueError("Ya existe un alumno con ese legajo.")

    self.repo.guardar(alumno)

Después, en `api.py`, convertí ese caso en una respuesta HTTP `409 Conflict`, en vez de dejar que termine como un error `500`.

**Ojo:** ahora `api.py` crea un `AlumnoService` nuevo en cada solicitud, y el repositorio guarda los alumnos en memoria. Así, un alumno agregado no se conserva para la siguiente solicitud. Si querés detectar duplicados entre solicitudes, necesitás mantener el repositorio compartido o usar una base de datos con una restricción única sobre `legajo`.
```

* El metodo agregar con la validacion en el alumno service quedo asi

```
    def agregar_alumno(self, alumno: Alumno) -> None:
        if self.repo.obtener_por_legajo(alumno.legajo) is not None:
            raise ValueError("Ya existe un alumno con ese legajo.")

        self.repo.guardar(alumno)
```

* Ahora vamos a devolver un stus http 409 en caso que haya un error

* Ahora en el api.py al agregar alumno devuelve un 409 si esta duplicado

```
    servicio = AlumnoService()
    try:
        servicio.agregar_alumno(alumno)
    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 409

```

---
# Break hasta y 25
---

## Testeo de Apis

* Hay varios programas o extensiones de chrome donde el dev puede testear una api (sin hacerlo desde el navegador)
  * Postman : el clasico, el prgograma mas comun para trabajar con APIs
  * Extension de VScode thuderclient
    * https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client
   
 > [!NOTA]
> El navegador nos alcanza cuando queremos prograr HTTP Get, pero cuando queremos probar, put, delete, y sobre todo armar el cuepo (body) de la peticion http en ese caso necesito un cliente distintinto, como Postman o Thuderclient

* Instalar thunderclient y problemos los endpoints

<img width="721" height="475" alt="image" src="https://github.com/user-attachments/assets/45a6986d-bf80-429a-8b0d-6924d247001a" />

* Vamos a probar el post
* Json del body
```
{
  "legajo": 6,
  "nombre": "Juan",
  "apellido": "Pérez",
  "fechaDeNacimiento": "2000-05-15"
}
```

> [!NOTE]
> Estara bueno que el legajo lo asigne solo el sistema

<img width="447" height="338" alt="image" src="https://github.com/user-attachments/assets/a84041ee-6a8f-4bc4-b11c-190e83d91b48" />

* Si luego recupero todos los alumnos deberia aparecer el nuevo, Juan Perez

> [!NOTE]
> Como cada endpoint crea un repositorio nuevo no lo guarda
---

# Receta crear un CRUD

* Como crer un CRUD con FLASK
  * Requerimiento : Instalar flask si no esta
  * Definir la estructura del proyecto : hacer un mermaid
  * Crear la estructura del proyecto
      * Crear la carpeta models
      * Crear la carpeta repositories
      * Crear la carpeta services
      * El archivo api.py
        * Podemos tener o no (A gusto) una carpeta tambien para la presentacion / controlador
  * Describir la estructura del proyecto e informacion de como me gusta trabajar en el Readme.md
      * Es importante contar con este archivo para darle contexto a la IA y no tener que repetirlo en cada prompt
 * Creamos la clase principal en models
      * Reglas de Negocio : Aca van las validaciones que aseguran que el objeto se mantiene consistente durante todo su ciclo de vida
 * Crearmos el repositorio
      * Persistimos el objeto ya sea en la base de datos, en archivos o en el mecanismo de persistencia que elijamos
      * Defino las operaciones que necesito para guardar, buscar y eliminar objetos del lugar donde los persistimos
      * En general esto es una base de datos
      * El modelo no accede al repositorio nunca
  * Creamos el servicio
      * Reglas de negocio: Creamos reglas que requieran el coordinar varias lllamadas al modelo y usar el repo
        * No hay legajo duplicado
  * Creo el endpoint de Flask
      * GET para todos
      * GET que recupera uno individualmente
      * POST para agregar uno nuevo
      * PUT para modificar
      * DELETE para borrar

## Trabajo Practico (Obligatorio)

* Quiero aplicando la receta y el ejemplo que vimos hagan un CRUD de una Persona que tiene DNI y nombre.
   * El documento no se puede repetir
   * El nombre comienza con mayucula y las otra otras con minuscula y no tiene mas de 30 caracteres
* Solo hacer los gets y el POST
* Probarlo con Thunder Client

* Subir el TP en su github (El mismo que me pasaron la primer clasa)

* Una vez subido completar la URL de github con el proyecto en el formulario quele pase el profe

* Subir el TP aca:
  * https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=FPbD6dnIlUCa1IfSyafYxE4uGCthyi9EnQYg85vv3slUOVlOSTNOUUJLRTIzQ081TFJHWTVaNDNZTS4u
  
---
# Proxim Clase - Poo - Metodos y atrbutos estaticos
# Vamos a hacerle un cliente a nuestro proyecto.
