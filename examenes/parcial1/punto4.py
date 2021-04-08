edades = [22, 19, 15, 20, 34, 28,49, 65,70, 45, 100, 68]

def datosLista (lista):
    print ("*"*30)
    print ("el numero mas grande es", max(lista))
    print ("el numero mas pequeño es", min (lista))
    print ("el promedio de la lista es", sum(lista)/(len(lista)))

datosLista (edades)
