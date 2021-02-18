#----entradas----#
MENSAJE_BIENDVENIDA = "bienvenido al codigo"
MENSAJE_MAYOR_EDAD = "eres mayor de edad, puedes seguir"
MENSAJE_MENOR_EDAD ="eres menor de edad, no puedes seguir"
PREGUNTA_EDAD = "cuantos años tienes : "

#---- codigos----#
print (MENSAJE_BIENDVENIDA)
edad = int(input (PREGUNTA_EDAD))
isMayor = edad >= 18
resultado = ""
if(isMayor):
    resultado = MENSAJE_MAYOR_EDAD
else:
    resultado = MENSAJE_MENOR_EDAD

print (resultado)
