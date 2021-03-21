#----entradas----#
MENSAJE_SALUDO = " bienvenido a este programa, juguemos!!! "
PREGUNTA_NUMERO = """
      en este juego debes acertar un numero entero
      que va desde el 1 al 10, la idea
      esque lo puedes intentar las veces 
      que quieras...
      muchos exitos!
"""
PREGUNTA_FALLASTE = "Ahhhh fallaste, ingresa otro numero : "
MENSAJE_GANASTE = "felicidades, ganaste!!"
MENSAJE_PERDISTE = "perdiste, vuelve a intentarlo"
MENSAJE_DESPEDIDA = "felicidades! ganaste"

#----entrada al codigo---#
numeroOculto = 7
vidas = 5
print(MENSAJE_SALUDO)
numeroIngresado = int(input(PREGUNTA_NUMERO))
if(numeroIngresado != numeroOculto):
    vidas -=1
while(numeroOculto != numeroIngresado and vidas > 0): 
    numeroIngresado = int(input(PREGUNTA_FALLASTE))
    vidas-= 1
if(vidas >= 0 and numeroOculto == numeroIngresado):
    print(MENSAJE_GANASTE)
    print(vidas)
else:
    print(MENSAJE_PERDISTE, "el numero era el", numeroOculto)