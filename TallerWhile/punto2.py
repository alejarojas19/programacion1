#----entradas----#
PREGUNTA_NUMERO_A = "ingresa un numero entero : "
PREGUNTA_NUMERO_B = "ingresa un numero entero mayor al que acabaste de ingresar : "

#----codigos----#
numeroA = int(input(PREGUNTA_NUMERO_A))
numeroB = int (input(PREGUNTA_NUMERO_B))

while ( numeroB > numeroA):
    numeroA = numeroB
    numeroB = int (input(PREGUNTA_NUMERO_B))   

if (numeroA >= numeroB):
    print("el segundo numero debe ser mayor")



