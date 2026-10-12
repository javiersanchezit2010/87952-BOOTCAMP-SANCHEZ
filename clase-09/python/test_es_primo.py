import es_primo

# Separar en casoss
# Generar Tests PAra
# Numero que no es primo devuelve false
# Un par de numeros primos devuelven true
# Si le pasas un string como parametro devuelve false

def test_es_primo_numeros_primos():
    assert es_primo.es_primo(2) is True
    assert es_primo.es_primo(3) is True
    assert es_primo.es_primo(5) is True


def test_es_primo_numeros_no_primos():
    assert es_primo.es_primo(4) is False
    assert es_primo.es_primo(1) is False


def test_es_primo_string():
    assert es_primo.es_primo("string") is False