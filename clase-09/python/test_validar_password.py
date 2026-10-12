
from validar_password import validar_password


def test_password_valida():
    resultado = validar_password("Abcdef1234!")

    assert resultado["valid"] is True
    assert resultado["message"] == "Password is valid"


def test_password_sin_numeros():
    resultado = validar_password("Abcdefghij!")

    assert resultado["valid"] is False
    assert resultado["message"] == "Password must contain numbers"


def test_password_sin_letras():
    resultado = validar_password("1234567890!")

    assert resultado["valid"] is False
    assert resultado["message"] == "Password must contain letters"


def test_password_menos_de_10_caracteres():
    resultado = validar_password("Abc123!x")

    assert resultado["valid"] is False
    assert resultado["message"] == "Password must be at least 10 characters"


def test_password_mas_de_20_caracteres():
    resultado = validar_password("Abcdefghijklmnop12345!")

    assert resultado["valid"] is False
    assert resultado["message"] == "Password must be at most 20 characters"


def test_password_sin_simbolo_especial():
    resultado = validar_password("Abcdef12345")

    assert resultado["valid"] is False
    assert resultado["message"] == "Password must contain a special symbol"


def test_password_sin_mayusculas():
    resultado = validar_password("abcdef1234!")

    assert resultado["valid"] is False
    assert resultado["message"] == "Password must contain uppercase letters"


def test_password_sin_minusculas():
    resultado = validar_password("ABCDEF1234!")

    assert resultado["valid"] is False
    assert resultado["message"] == "Password must contain lowercase letters"


def test_password_con_espacios():
    resultado = validar_password("Abc 123456!")

    assert resultado["valid"] is False
    assert resultado["message"] == "Password must not contain spaces"
