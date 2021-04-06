listaNumeros = [1,2,3, 4,5,6,7,8,9,10,11,12,13,14,15]

def numerosPares (lista):
    listaNumerosPares = []
    for elemento in lista:
        if elemento % 2 == 0:
            listaNumerosPares.append (elemento)
    return listaNumerosPares

print (numerosPares (listaNumeros))

