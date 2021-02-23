#----constantes----#
MENSAJE_SALUDO = "Hola! Ingresa los siguientes valores para ver en que estado se encuentra el paciente"
PREGUNTA_TRIGLICERIDOS = "ingresa los niveles de trigliceridos : "
PREGUNTA_HOMOCISTEINA = "ingresa los niveles de homocisteina : "
RESPUESTA_OPTIMO_HOMOCISTEINA = "los niveles de homocisteina son optimos"
RESPUESTA_SOBRE_LIMITE_HOMOCISTEINA = "los niveles de homocisteina estan sobre el limite"
RESPUESTA_HOMOCISTEINA_ALTO = "los niveles de homocisteina son altos"
RESPUESTA_HOMOCISTEINA_MUY_ALTO = "los niveles de homocisteina son muy altos"
RESPUESTA_OPTIMO_TRIGLICERIDOS = "los niveles de trigliceridos son optimos"
RESPUESTA_SOBRE_LIMITE_TRIGLICERIDOS = "los niveles de trigliceridos estan sobre el limite"
RESPUESTA_TRIGLICERIDOS_ALTO = "los niveles de trigliceridos son altos"
RESPUESTA_TRIGLICERIDOS_MUY_ALTO = "los niveles de trigliceridos son muy altos"
MENSAJE_DESPEDIDA = "espero te haya sido de gran ayuda este codigo"

#----entradas----#
print(MENSAJE_SALUDO)
trigliceridos = float(input(PREGUNTA_TRIGLICERIDOS))
homocisteina = float (input(PREGUNTA_HOMOCISTEINA))

#----codigos----#
isOptimoT = trigliceridos < 150
isLimite = trigliceridos >= 150 and trigliceridos <= 199
isAlto = trigliceridos >=200 and trigliceridos <= 499
isMuyAlto = trigliceridos > 500
isOptimoH = homocisteina > 2 and homocisteina <=15
isLimiteH = homocisteina > 15 and homocisteina <= 30
isAltoH = homocisteina >30 and homocisteina <=100
isMuyAltoH = homocisteina > 100

if(isOptimoT) :
    print(RESPUESTA_OPTIMO_TRIGLICERIDOS)
elif(isLimite):
    print(RESPUESTA_SOBRE_LIMITE_TRIGLICERIDOS)
elif(isAlto):
    print(RESPUESTA_TRIGLICERIDOS_ALTO)
else:
    print(RESPUESTA_TRIGLICERIDOS_MUY_ALTO)

if(isOptimoH):
    print(RESPUESTA_OPTIMO_HOMOCISTEINA)
elif(isLimiteH):
    print(RESPUESTA_SOBRE_LIMITE_HOMOCISTEINA)
elif(isAltoH):
    print(RESPUESTA_HOMOCISTEINA_ALTO)
else:
    print(RESPUESTA_HOMOCISTEINA_MUY_ALTO)
print(MENSAJE_DESPEDIDA)
