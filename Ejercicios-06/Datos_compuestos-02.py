# Datos compuestos 02
"""
2.- Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por
pantalla.
"""
asignaturas=[]
op=1
while op != 0:
    print("-------------------------")
    print("Quieres escribir algo en la lista asignaturas?")
    op=int(input("1 para si, 0 para no: "))
    if op ==1:
        agrega=input("Que materia desea agregar? ")
        asignaturas.append(agrega)
        print("-------------------------")
        print(asignaturas)
    if (op == 0):
        print("La lista final quedaria asi: ")
        print("-------------------------")
        print(asignaturas)
        print("-------------------------")
        print("See you next round")
    if (op != 0 and op != 1):
        print("No escribiste un 1 o un 0")
        print("-------------------------")

