# Clase 15 - 28 de Septiembre del 2026

# Repaso

* Arquitectura de Sistema
  * POO
    * Consistencia de Objetos
      * Constructores
      * Getters / Setters
    * Relaciones entre Objetos
      * Cardinalidad entre las Relaciones
  * Diseño por capas
    * Presentacion
    * Dominio
    * Persistencia
  * UML
    * Diagrama de Clases

---

# HTTP 

* https://www.instagram.com/p/DMMcfavuN58/?img_index=1
* El usuario se conecta mediante el navegador a una pagina web utilizando el protobolo HTTP para que el servidor web le devuelva una pagina HTML
* Es un protocolo STATELESS
* Tiene Metodos
  * GET
    * Pido informacion del servidor
    * (No manda body)
  * POST
    * (manda BODY)
    * Mandar informacion al servidor
* Arquitectura Cliente-Servicor
  * Cliente
    * WebBrowser
     * Chrome
     * Chromium
     * Brave
     * Opera
  * Servidor
    * WebServer
     * Apache
     * Nginx
     * IIS (Internet Information Server)
  * El cliente se comunica con el servidor por el protocolo HTTP

  * Mira esta pagina para ver los errores HTTP
    * https://http.cat/
 
  * Experiencia
     * Abrir el Chrome
     * Abrir las Dev Tools (F12)
     * Mirar las solapas que tienen las dev toools
     * Navegar mi pagina web favorita
     * Explorar las peticiones en la solapa networking

<img width="592" height="444" alt="image" src="https://github.com/user-attachments/assets/de0e385d-a373-4450-84df-eea6c87e5e49" />

---
BREAK
Hasta y 25
---

# Ejemplo Practico de la arquitectura en capas

* Vamos a desarrollar un CRUD con API rest
  * CRUD (CREATE READ UPDATE DELETE) en criollo se le dice ABM (Alta Baja modificacion)
  * Vamos a ser un CRUD
* Arquitectura
  * Presentacion
      * API Rest
      * Hecha en Flask
      * Endpoints
  * Dominio / Modelo
    * Clase Alumno
  * Persistencia
    * Clase RepositorioAlumnos
    * Por ahora guarda mis alumnos en memoria

---

## Primero arranquemos con Flask

* Hoy trabamos en local
  * Vamos a preparar un vscode en una carpeta local
  * Lo  podemos probar con un Gola Mundo

### API Rest

* Es una API (interfaz de programación de aplicaciones) que funciona sobre el protocola HTTP recibiendo y enviando informacion en JSON
  * A mi me gusta pensarlo como una pagina web sin interfaz grafica.
  * En lugar de devolver HTML devuelvo JSON
  * Esta pensada no para que la consuma un usuario final, sino que sea consumida por otro programa
  * Utiliza HTTP y las acciones HTTP (
     * GET
       * Solo devuelve
     * POST
     * PUT
     * DELETE

* Ejemplos de API rest
  * https://rickandmortyapi.com/api/character
  * https://pokeapi.co/api/v2/pokemon
  * https://jsonplaceholder.typicode.com/
  * https://www.instagram.com/p/ChF6pu8u6cm/?img_index=1 << Una lista completa
 
### Nuestra primera API Flask

* Se la pedimos a la IA : "haceme un hola mundo en flask"

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True)
```

* Debemos instlar Flask si  no lo instalamos previamente

```
pip install flask
```

* PAra ejecutarlo

```
>python demo-api.py
 * Serving Flask app 'demo-api'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with watchdog (windowsapi)
 * Debugger is active!
 * Debugger PIN: 146-162-111
```

 * Esto inicia un webserver en el puerto 5000 (La app funciona como si fuera un apache)

 * Luego escribo en el navegador

```
http://127.0.0.1:5000
```

* Deberia mostrar en el navegador un "Hola mundo". Esto hace una peticion GEt

```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.11.1
Date: Mon, 28 Sep 2026 23:53:00 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 10
Connection: close
```

* Visualizar y explorar esa peticion con los Dev Tools

<img width="593" height="421" alt="image" src="https://github.com/user-attachments/assets/ef3c5f1f-78f4-494b-8392-df264490fdd9" />

* Prestarle atencion al content-type (mime) donde veos que la respuesta es de tipo texto

* Vamos a agregar otro endpoint esta vez que devuela un json con IA : agregar un endpoint persona que devuelva una persona represetnada en un json

```
@app.route("/persona")
def persona():
    return {
        "nombre": "Esteban",
        "apellido": "Calabria",
        "edad": 44
    }
```

* Cuando devuelvo un diccionario Flask automaticamente lo conviernte a una respuesta en JSON. Accedo como

```
http://127.0.0.1:5000/persona
```

* Ahora si miramos la petticion HTTP

```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.11.1
Date: Tue, 29 Sep 2026 00:01:54 GMT
Content-Type: application/json
Content-Length: 66
Connection: close
```

* Ahora el content-type es un json

---

* En el proximo ejemplo quiero trabar con objetos. Entonces no voy a devolver un diccionario, voy a devolver la isntancia de un objeto. Quiero que flask me a convierta ajson
* Se lo vamos a pedir a la IA : "Ahora quiero un endpoint alumno que devuelva un json de un alumno pero que dentro del codigo no lo cree como un diccionario sino como una instancia de la clase alumno. Dame el endpoint y la clase"


```
class Alumno:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


@app.route("/alumno")
def alumno():
    alumno = Alumno("Juan", "Pérez", 25)

    return {
        "nombre": alumno.nombre,
        "apellido": alumno.apellido,
        "edad": alumno.edad
    }

```

* Esto que hizo la IA esta masomenos
  * No asegura la consistencia del objeto
  * Tambien vamos a ver que podemos crear el diccionario automaticamente sin tener que hacerlo manual
 
### Serializar objetos a JSON

* En el ejemplo anterior, el diccionario se tiene que crear manualmente de todas maneras
* Si queremos automatizar el proceso de convertir una instancia en un diccionario, ese proceso se llama serializacion
  * Estariamos serializando/convirtiendo un objeto en un diccionario (Solamente los atributos)
 
* Para ello tenemos que usar en python el metodo jsonify, asdict y decorar nuestra clase con @dataclass
* Los import ahora me quedarian

```
from flask import Flask, jsonify
from dataclasses import asdict, dataclass
```

* La clase la decoro con @dataclass y defino sus atributos

```
@dataclass
class Alumno:
    nombre : str
    apellido : str
    edad : int
```

* No le pusimos el metodo init para hacerla mas sencillo, pero desde la perspectiva de las buenas practicas de la poo esta clase esta maso maso

* Modificamos el endopoint para no tener que crear el diccionario a mano

```
@app.route("/alumno")
def alumno():
    alumno = Alumno("Juan", "Perez", 25)
    return jsonify(asdict(alumno))
```

---

# Proxima Clase

* Nos quedo pendiente armar todo con la arquitectura en capas! Como no habia dado antes lo de HTTP tuve que hacer un parentesis y darlo
