from funciones import sumar

def test_sumar_dos_numeros_positivos():
    assert sumar(2, 4) == 5


def test_sumar_numeros_negativos():
    assert sumar(-2, -3) == -5


def test_sumar_positivo_y_negativo():
    assert sumar(5, -2) == 3


def test_sumar_con_cero():
    assert sumar(5, 0) == 5

def test_sumar_cero_y_cero():
    assert sumar(0, 0) == 0