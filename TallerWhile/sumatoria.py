#----entradas----#
MENSAJE_BIENVENIDA = "Hola, ingresa los datos y ayudame a estuadiar"
PREGUNTA_NUMERO = "ingresa un numero entero o 0 para terminar: "
MENSAJE_DESPEDIDA = "que estes bien, gracias"

#----codigos----#
print (MENSAJE_BIENVENIDA)
numeroIngresado = int(input(PREGUNTA_NUMERO))
sumatoria = 0
while(numeroIngresado != 0):
    sumatoria += numeroIngresado
    numeroIngresado = int (input(PREGUNTA_NUMERO))
print(sumatoria)
print(MENSAJE_DESPEDIDA)


