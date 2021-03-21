#----constantes----#
MENSAJE_BIENVENIDA = "hola, espero estes bien"
MENSAJE_AÑO_ACTUAL = "Ingrese el año actual : "
MENSAJE_AÑO = "Ingrese otro año cualquiera : "
MENSAJE_IGUALES = "los años ingresados son iguales"

#----codigos----#
print(MENSAJE_BIENVENIDA)
añoActual = int(input(MENSAJE_AÑO_ACTUAL))
añoX = int (input(MENSAJE_AÑO))
if(añoActual > añoX): 
    restar = añoActual - añoX
    print ( "han pasado", restar, "años")
elif(añoX > añoActual):
    restar = añoX - añoActual
    print ("faltan", restar, "años")
else:
    print (MENSAJE_IGUALES)
