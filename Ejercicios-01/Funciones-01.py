# Funciones 01
"""
1.- Realiza una función llamada area_rectangulo(base, altura) que devuelva el área
del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de
15 de base y 10 de altura.
"""

base = 15
altura = 10

def area_rectangulo(base,altura):
    res = base * altura
    return res

print(f"el area del rectangulo es: {area_rectangulo(base,altura)}")

# Ahora le pedimos los valores a usted

base = float(input("Ingresa el valor de la base: "))
altura = float(input("Ingresa el valor de la altura: "))

print(f"el area del rectangulo con sus valores es: {area_rectangulo(base,altura)}")

