PREGUNTA_NUMERO = "ingrese un numero : "
listaNumeros = []
listaPositivos = []
listaNegativos = []
for i in range (6):
    numero = int(input(PREGUNTA_NUMERO))
    listaNumeros.append(numero)
    if (numero >= 0):
        listaPositivos.append(numero)
    else:
        listaNegativos.append(numero)
print (listaNumeros)
print(listaNegativos)
print (listaPositivos)
suma = sum(listaNegativos)
promedio = sum(listaPositivos)/len(listaPositivos)
print("la suma de los negativos es", suma)
print ("el promedio es", promedio)

