PREGUNTA_NUMERO = "ingresa un numero entero positivo : "
factorial = 1 
numeroIngresado = int(input(PREGUNTA_NUMERO))

for iteracion in range (numeroIngresado):
    factorial = factorial * (iteracion + 1)
print (factorial)