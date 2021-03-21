#----constantes----#
MENSAJE_BIENDVENIDA = "hola, ayudame llenando la siguiente información"
PREGUNTA_NUMERO_A = "Ingrese número A : "
PREGUNTA_NUMERO_B = "ingrese numero B : "
MENSAJE_MAYOR = "el numero A es mayor que el numero B"
MENSAJE_MENOR = "el numero A es menor que el numero B"
MENSAJE_IGUAL = " el numero A es igual que el numero B"
MENSAJE_DESPEDIDA = "Gracias, que estes bien"

#----codigos----#
print (MENSAJE_BIENDVENIDA)
numeroA = int(input(PREGUNTA_NUMERO_A))
numeroB = int(input(PREGUNTA_NUMERO_B))
isMayor = numeroA > numeroB
isMenor = numeroA < numeroB
isIgual = numeroA == numeroB 
resultado = ""
if(isMayor):
    resultado = MENSAJE_MAYOR
elif(isMenor):
    resultado= MENSAJE_MENOR
else:
    resultado = MENSAJE_IGUAL
print (resultado)
print (MENSAJE_DESPEDIDA)

