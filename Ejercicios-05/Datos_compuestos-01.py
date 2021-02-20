# Datos compuestos 01
"""
1.- Realiza una función separar(lista) que tome una lista de números enteros
desordenados y devuelva dos listas ordenadas. La primera con los números pares y la
segunda con los números impares.
"""

numeros = []
for var in range(int(input("Cuantos numeros agregaras a la lista? "))):
    numeros.append(input(f"Agrega el registro {var+1}: "))

pares = []
impares = []

def separar(numeros):
    for var in numeros:
        if int(var)%2==0:
            pares.append(int(var))
        elif int(var)%2 == 1:
            impares.append(int(var))

separar(numeros)
print(f"Lista de numeros: {numeros}")
print(f"Lista de pares desordenados: {pares}\nLista de impares desordenados: {impares}")

pares_ordenados = sorted(pares)
impares_ordenados = sorted(impares)

print(f"Lista de pares ordenados: {pares_ordenados}")
print(f"Lista de impares ordenados: {impares_ordenados}")
