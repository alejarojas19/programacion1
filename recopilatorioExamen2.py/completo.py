#----entradas----#
preguntaNumero = """ ingrese alguna de estas opciones
                    1. Hacer conversion de dolares a pesos o euros
                    2. Categoria de ingresos
                    3. mostrar ingreso mas alto, mas bajo y promedio
                    4. salir
"""
preguntaMoneda = """
                    C- mostar lista en pesos
                    D- mostar lista original en dolares
                    E- mostar lista en euros
"""
#----conversiones----# 
listaDolares = [20000, 30000, 4000, 2500, 1000, 7600 ]
listaPesos = []
for elemento in listaDolares:
    listaPesos.append(elemento*3700 )
listaEuros = []
for elemento in listaDolares:
    listaEuros.append(elemento* 0.84) 

#----codigos----#
opcionEscogida = int(input(preguntaNumero))
listaDolares = [20000, 30000, 4000, 2500, 1000, 7600 ]
while(opcionEscogida != 4):
    opcionEscogida = int(input(preguntaNumero)) 
    #-----opcion 1----#
    if(opcionEscogida == 1):
        opcionMoneda = input(preguntaMoneda)
        if (opcionMoneda == "C"):
            print("mostarndo lista en pesos")
            print(listaPesos)
        elif (opcionMoneda == "D"):
            print("mostarndo lista original")
            print(listaDolares)
        elif (opcionMoneda == "E"):
            print("mostrando lista en euros")
            print(listaEuros)
        else:
            print ("ingrese una opcion valida")
    #----opcion 2----#
    elif(opcionEscogida == 2):
        for elemento in listaDolares:
            if (elemento < 1000):
                print("ingresos bajos")
            elif(elemento > 1000 and elemento < 7000): 
                print ("ingresos medios")
            elif(elemento > 7000 and elemento < 20000):
                print("ingresos altos")
            else:
                print("ingresos elevados")
    #----opcion 3----#
    elif(opcionEscogida == 3):
        mayor = max (listaDolares)
        menor = min (listaDolares)
        acumulador = 0
        for elemento in listaDolares :
            acumulador += elemento
            promedio= acumulador/len(listaDolares)
    else:
        print ("error numero")

opcionEscogida = int(input(preguntaNumero)) 
print("salida del menu")
