#----entradas----#
MENSAJE_BIENVENIDA = "muy uenos dias, despierte que esta en clase de 6"
MENSAJE_ERROR = " porfavor ingrese una opcion valida"
PREGUNTA_MENU = """ ingrese
    1 - para mostrar los numeros de 1 - 5
    2 - para preguntar tu nombre
    3 - para mostrar el año en el que estamos 
    4 - salir
"""
PREGUNTA_NOMBRE = "ingrese el nombre porfavor"
entrada = 1
while(entrada >= 1 and entrada <= 3):
    entrada = int(input(PREGUNTA_MENU))
    print(entrada)
    if(entrada == 1):
        print (1, 2, 3, 4, 5)
    elif (entrada == 2):
        nombre = input(PREGUNTA_NOMBRE)
        print (f"bienvenido {nombre} a este menu, emplea las otras opciones")
    elif (entrada == 3):
        print ("estamos en el año 2021")
    elif (entrada == 4):
        print("muchas gracias por usar el programa")
    else:
        entrada = 1
        print("MENSAJE_ERROR")





