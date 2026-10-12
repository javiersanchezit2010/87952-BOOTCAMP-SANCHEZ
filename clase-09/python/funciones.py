def sumar(a, b):
  return a + b

def multiplicar(a, b):
  return a * b

def dividir(a,b):
   return a/b

def num_mayor(lista):
  if not lista:
    return None

  mayor = lista[0]
 
  for num in lista:
    if num > mayor:
       mayor = num
 
  return mayor


def es_par(numero):
 if isinstance(numero, int):
    return numero % 2 == 0
 else:
    return "Debes ingresar un número"


def saludo(name):
   return (f"Hola, {name}! Esta es una función en Python.")

def duplicar_lista(numeros):
    return [numero * 2 for numero in numeros]

def es_par(numero):
  if numero % 2 == 0:
    return True
  else:
    return False