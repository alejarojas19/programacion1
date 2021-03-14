#----constantes----#
PREGUNTA_NUMEROA = "ingrese numero A : "
PREGUNTA_NUMEROB = "ingrese numero B : "
MENSAJE_BIENVENIDA = "hola! Ingresa los siguientes datos"
MENSAJE_DESPEDIDA = "gracias! Que tengas un lindo día"

#---- codigos ----#
print (MENSAJE_BIENVENIDA)
numeroA = int(input(PREGUNTA_NUMEROA))
numeroB = int(input(PREGUNTA_NUMEROB))
isNumeroaMayor = numeroA > numeroB
print ("#"*10 , "el numeroA es mayor que el numeroB" , "#"*10)
print (isNumeroaMayor)
isNumeroaMenor = numeroA< numeroB
print ("#"*10 , "el numeroA es menor que el numeroB" , "#"*10)
print (isNumeroaMenor)
isIgual = numeroA == numeroB
print ("#"*10 , "el numeroA es igual que el numeroB" , "#"*10)
print (isIgual)
isDiferente = numeroA != numeroB
print ("#"*10 , "el numeroA es diferente que el numeroB" , "#"*10)
print (isDiferente)
sumar = numeroA + numeroA
print (f"el resultado de la suma es {sumar}")
restar = numeroA - numeroB
print (f"el resultado de la resta es {restar}")
multiplicar = numeroA * numeroB
print (f"el resultado de la multiplicacion es {multiplicar}")
dividir = numeroA/numeroB
print (f"el resultado de la division es {dividir}")
potencia = numeroA ** numeroB
print (f"el resultado de la potenciacion es {potencia}")
print (MENSAJE_DESPEDIDA)


