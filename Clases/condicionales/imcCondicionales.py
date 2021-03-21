#----constantes ---#
PREGUNTA_PESO = "cuanto pesas en kg? : "
PREGUNTA_ESTATURA = "cuanto mides en m : "
MENSAJE_BIENVENIDA = "Hola, como estas?, voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "tu IMC es..."
MENSAJE_BAJO_PESO = "estas bajo peso"
MENSAJE_PESO_NORMAL = "estas en forma"
MENSAJE_SOBREPRESO = "ten cuidado, estas en sobrepeso"
MENSAJE_OBESO = "ten cuidado, estas obeso"

#--- codigo ---#
print (MENSAJE_BIENVENIDA)
peso = float(input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
IMC = peso/(estatura**2)
isBajoPeso = IMC < 18.5
isNormal = IMC >= 18.5 and IMC < 25
isSobrePeso = IMC >=25 and IMC < 30 
resultado = ""
if(isBajoPeso):
    resultado = MENSAJE_BAJO_PESO
elif(isNormal):
    resultado = MENSAJE_PESO_NORMAL
elif(isSobrePeso):
    resultado = MENSAJE_SOBREPRESO
else:
    resultado = MENSAJE_OBESO
print(MENSAJE_DESPEDIDA, IMC)
print (resultado)
