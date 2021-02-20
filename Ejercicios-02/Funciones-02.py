# Funciones 02
"""
2.- Realiza una función llamada area_circulo(radio) que devuelva el área de un
círculo a partir de un radio. Calcula el área de un círculo de 5 de radio.
"""
import math

radio = 5

def area_circulo(radio):
    area = radio * radio * math.pi
    return area

print(area_circulo(radio))

# Ahora el usuario escribe el radio del circulo

radio = float(input("Escribe el valor del radio: "))

print(f"El valor del area del circulo es: {area_circulo(radio)}")