#----constantes----#
MENSAJE_BIENVENIDA = "hola! espero estes super bien"
PREGUNTA_EDAD = "cuantos años tienes? : "
MENSAJE_MENOR_EDAD = "eres menor de edad"
MENSAJE_JOVEN = "eres joven"
MENSAJE_ADULTO = "eres adulto"
MENSAJE_MAYOR = "eres adulto mayor"
MENSAJE_DESPEDIDA = "que tengas un lindo dia"
#----codigos----#
print (MENSAJE_BIENVENIDA)
edad = int (input (PREGUNTA_EDAD))
respuesta = ""
if(edad < 18): 
    respuesta = MENSAJE_MENOR_EDAD
elif(edad >= 18 and edad <= 25):
    respuesta = MENSAJE_JOVEN
elif(edad >= 26 and edad <= 60):
    respuesta = MENSAJE_ADULTO
else:
    rspuesta = MENSAJE_MAYOR
print (respuesta)
print (MENSAJE_DESPEDIDA)