# Datos compuestos 03
"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a
mayor.
Escribir un programa que almacene en una lista los números del 1 al 10 y los
muestre por pantalla en orden inverso separados por comas.
"""
loteria = []

print("La loteria primitiva consta de 7 numeros que van del 1 al 49")

for i in range(0,7):
    bola=-1
    while(not(bola >= 1 and bola <= 49)):
        bola = int(input(f"Dame el valor de la bola {(i+1)}: "))
        if bola >=   50:
            print("La loteria primitiva va de 1 a 49")
        if bola == 0:
            print("La loteria primitiva va de 1 a 49")
        if bola < 0:
            print("Aqui no aceptamos numeros negativos")

    loteria.append(bola)    

    lista_ordenada = sorted(loteria)
    print("----------------------------------")
    print("La lista ordenada de la loteria es: ")
    print(lista_ordenada)
    print("----------------------------------")
print("\n------------------------------------------------------------------------")
print("Ahora te cruzo una lista con los numeros del 1 al 10 en el orden inverso")
#a listado la hacemos una lista que contenga el rango del 1 al 11, que va del 1 al 10
listado=list(range(1,11))
#a listado le invertimos el orden para que parezca que es de menor a mayor, que lo es
listado.sort(reverse=True)
#creamos una tupla con los elementos que tiene listado
tuplado=tuple(listado)
print(tuplado)
print("-------------------------------")
print("Puuuuuum")
