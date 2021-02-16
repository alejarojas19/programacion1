#----constantes ---#
PREGUNTA_PESO = "cuanto pesas en kg? : "
PREGUNTA_ESTATURA = "cuanto mides en m : "
MENSAJE_BIENVENIDA = "Hola, como estas?, voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "tu IMC es..."

#--- codigo ---#
print (MENSAJE_BIENVENIDA)
peso = float(input(PREGUNTA_PESO))
estatura = float(input(PREGUNTA_ESTATURA))
IMC = peso/(estatura**2)
print (MENSAJE_DESPEDIDA, IMC)
isObeso = IMC >= 30
print ("el resultado de la prueba de obesidad es...", isObeso)