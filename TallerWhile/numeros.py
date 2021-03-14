#----entradas----#
MENSAJE_BIENVENIDA = "Hola, ingresa los datos y ayudame a estudiar"
PREGUNTA_NUMERO_A = "ingresa un numero entero A : "
PREGUNTA_NUMERO_B = "ingresa un numero entero B menor al numero anterior : "
MENSAJE_ERROR = "recuerda ingresar un numero menor que el primero que ingresaste"
MENSAJE_DESPEDIDA = "gracias, que estes bien"

#----codigos----#
numeroA = int(input(PREGUNTA_NUMERO_A))
numeroB = int(input(PREGUNTA_NUMERO_B))

while(numeroB < numeroA):
    numeroB = int(input(PREGUNTA_NUMERO_B))
    if (numeroB > numeroA):
        print (MENSAJE_ERROR)

print (MENSAJE_DESPEDIDA)
