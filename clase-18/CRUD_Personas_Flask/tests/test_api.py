import unittest

from api import app, repository


class PersonaAPITestCase(unittest.TestCase):
    def setUp(self):
        repository.limpiar()
        self.client = app.test_client()

    def test_listar_personas_inicialmente_vacio(self):
        response = self.client.get("/personas")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_crear_y_obtener_persona(self):
        response = self.client.post(
            "/personas",
            json={"dni": "30123456", "nombre": "Javier"},
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {"dni": "30123456", "nombre": "Javier"})

        response = self.client.get("/personas/30123456")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"dni": "30123456", "nombre": "Javier"})

    def test_rechaza_dni_duplicado(self):
        datos = {"dni": "30123456", "nombre": "Javier"}
        self.client.post("/personas", json=datos)

        response = self.client.post(
            "/personas",
            json={"dni": "30123456", "nombre": "María"},
        )

        self.assertEqual(response.status_code, 409)
        self.assertIn("error", response.get_json())

    def test_rechaza_nombre_invalido(self):
        response = self.client.post(
            "/personas",
            json={"dni": "30123456", "nombre": "JAVIER"},
        )

        self.assertEqual(response.status_code, 400)

    def test_rechaza_nombre_mayor_a_30_caracteres(self):
        response = self.client.post(
            "/personas",
            json={"dni": "30123456", "nombre": "A" + "a" * 30},
        )

        self.assertEqual(response.status_code, 400)

    def test_busqueda_inexistente_devuelve_404(self):
        response = self.client.get("/personas/no-existe")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
