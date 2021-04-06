listaNumeros = [11,12,24,25,28,20,35,67]
listaNumeros2 = [1,45,34,23,78,54,33,12]

def numerosMayores (lista):
    listaMayores = []
    for elemento in lista:
        if elemento > 24:
            listaMayores.append (elemento)
    return listaMayores


print (numerosMayores(listaNumeros))
print (numerosMayores(listaNumeros2))
