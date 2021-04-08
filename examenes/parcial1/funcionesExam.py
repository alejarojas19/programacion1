
def operaciones (operacion, valor1, valor2, valor3):
    print (operacion(valor1, valor2, valor3))

def listado (lista1, lista2, lista3):
    print (lista1, lista2, lista3)

def area (preguntaBase, preguntaAltura):
    areaTriangrulo = (preguntaBase * preguntaAltura)/2
    return areaTriangrulo

def datosLista (lista):
    print ("*"*30)
    print ("el numero mas grande es", max(lista))
    print ("el numero mas pequeño es", min (lista))
    print ("el promedio de la lista es", sum(lista)/(len(lista)))
