import random
#----entradas----#
MENSAJE_SALUDO = " bienvenido a este programa, juguemos!!! "
PREGUNTA_NUMERO = """
      en este juego debes acertar un numero entero
      que va desde el 1 al 10, la idea
      esque lo puedes intentar antes de que se te acaben las vidad,
      no existe vide 0...
      muchos exitos!
"""
PREGUNNTA_DIFICULTAD = """
     1 - facil
     2- moderado
     3 - dificil 
"""
PREGUNTA_FALLASTE = "Ahhhh fallaste, ingresa otro numero : "
MENSAJE_GANASTE = "felicidades, ganaste!!"
MENSAJE_PERDISTE = "perdiste, vuelve a intentarlo"

#----entrada al codigo----#
numeroOculto = random.randint (1,10)
vidas = None

dificultad = int (input(PREGUNNTA_DIFICULTAD))
while(dificultad != 1 and dificultad != 2 and dificultad !=3):
    print ("ingresa una opcion valida")
    dificultad = int (input(PREGUNNTA_DIFICULTAD))

if(dificultad == 1):
    print ("modo facil activado")
    vidas = 5
elif(dificultad == 2):
    print ("modo moderado activado")
    vidas = 3
else:
    print("modo dificil activado, ssss mucho cuidado")
    vidas = 1

numeroIngresado = int(input(PREGUNTA_NUMERO))
while (numeroIngresado != numeroOculto and vidas > 1):
    vidas -= 1
    print (f"te quedan {vidas} vidas")
    numeroIngresado = int(input(PREGUNTA_FALLASTE))

if( vidas >= 0 and numeroIngresado == numeroOculto):
    print (MENSAJE_GANASTE)
else: 
    print (MENSAJE_PERDISTE, "el numero era ", numeroOculto)
