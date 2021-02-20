# Funciones 03
"""
Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo
siguiente (Quizá debas adelantarte un poco al uso de condiciones básicas):

● Si el primer número es mayor que el segundo, debe devolver 1.
● Si el primer número es menor que el segundo, debe devolver -1.
● Si ambos números son iguales, debe devolver un 0.

Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.
"""
a = float(input("Escriba el valor del primer numero: "))
b = float(input("Escriba el valor del segundo numero: "))

def relacion(a,b):
    res=0
    if (a > b):
        res = 1
    elif (a < b):
        res = -1
    elif (a == b):
        res = 0
    else:
        res = "Como llegaste hasta aqui?" #Tecnicamente nunca ejecutara esta parte
    return res

print(relacion(a,b))