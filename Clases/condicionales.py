#---- constantes ----#
MENSAJE_BIENDVENIDA = "Hola, espero que estes bien"
PREGUNTA_NUMERO_A = "ingrese un numero A : "
pregunta_NUMERO_B = "ingrese numero B : "
MENSAJE_MAYOR = "el numero A es mayor que el numero B"
MENSAJE_MENOR = "el numero A es mejor que el numero B"
MENSAJE_IGUAL = "el numero A es igual al numero B"

#---- codigos ----#
print (MENSAJE_BIENDVENIDA)
numeroA = int(input(PREGUNTA_NUMERO_A))
numeroB = int(input(pregunta_NUMERO_B))
isMayor = numeroA > numeroB
isMenor = numeroA < numeroB
resultado = ""

if(isMayor):
    resultado = MENSAJE_MAYOR
elif (isMenor):
    resultado = MENSAJE_MENOR
else:
    resultado = MENSAJE_IGUAL

print (resultado)
