from funciones import num_mayor


def test_num_mayor_lista_con_numeros_positivos():
    assert num_mayor([3, 8, 1, 6]) == 8


def test_num_mayor_lista_con_numeros_negativos():
    assert num_mayor([-10, -3, -7, -1]) == -1


def test_num_mayor_lista_con_mixto_positivos_y_negativos():
    assert num_mayor([-5, 0, 12, -2, 7]) == 12


def test_num_mayor_lista_con_un_solo_elemento():
    assert num_mayor([42]) == 42


def test_num_mayor_lista_ordenada_descendente():
    assert num_mayor([9, 7, 5, 3, 1]) == 9


def test_num_mayor_lista_ordenada_ascendente():
    assert num_mayor([1, 3, 5, 7, 9]) == 9


def test_num_mayor_lista_vacia():
    assert num_mayor([]) == None
