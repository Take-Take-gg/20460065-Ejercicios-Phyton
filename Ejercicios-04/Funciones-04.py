# Funciones 4
"""
4.- Realiza una función llamada intermedio(a, b) que a partir de dos números,
devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio
entre -12 y 24:
Pista: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
"""
a= float(input("Ingrese el valor de \"a\":" ))
b= float(input("Ingrese el valor de \"b\":" ))

def intermedio(a,b):
    res = (a+b)/2
    return res

print(f"El punto intermedio es: {intermedio(a,b)}")
# print("El punto intermedio entre "+a+" y "+b+ f" es: {intermedio(a,b)}")
# print("El punto intermedio entre" + str(a) + " y " + str(b) + " es: " + str(intermedio(a,b)))