temperaturaCorporal = [36, 37, 38, 35, 36, 38, 37.5, 38.2, 41,37.4, 38.6,39.1, 40.3, 33]


#----mensajes----#
preguntaNumero = """ingrese alguna de estas opciones
                    1- convertir temperaturas
                    2- mostar si la temperatura es saludable o no
                    3- temperatura maxima o minima
                    4- salir 
""" 
preguntaTemperatura = """
                        F- fahrenheit (°F)
                        K- kelvin (°K)
                        C- celcius (°C)
"""
mensajeMayor = "La temperatura mas alta es --> "
mensajeMenor = "La temperatura mas baja es --> "
mensajeHora = "La temperatura se tomo cada"

#----primer punto----#
entradaMenu = int (input (preguntaNumero))
temperaturaConvertida = []
temperaturaSaludable = []

if (entradaMenu) == 1:
    unidad (temperaturaCorporal)
elif (entradaMenu) == 2:
    for temperatura in temperaturaCorporal:
        if (temperatura < 36):
            temperaturaSaludable.append ("tiene hipotermia")
            print ("tiene hipotermia", temperatura) 
        elif (temperatura > 37.6 ):
            temperaturaSaludable.append ("tiene fiebre")
            print ("tiene fiebre", temperatura)
        else:
            temperaturaSaludable.append ("esta saludable")
            print ("temperatura normal", temperatura)
    print (temperaturaSaludable)
elif (entradaMenu) == 3:
    print ("la temperatura maxima es", max(temperaturaCorporal))
    print ("la temperatura minima es", min(temperaturaCorporal))
    print ("la temperatura se tomo cada ", 24/len(temperaturaCorporal), "horas")
else:
    print ("salir")



def unidad (lista):
    Preguntatemperatura2 = input(preguntaTemperatura)
    for temperatura in lista:
        if (Preguntatemperatura2 == "F"):
            temperatura = (temperatura * 1.8) + 32
            temperaturaConvertida.append (temperatura)
        elif (Preguntatemperatura2 == "K"):
            temperatura = temperatura + 273.15
            temperaturaConvertida.append(temperatura)
    if (Preguntatemperatura2 == "C"):
        print ("la temperatura ya esta en celcius")
    else:
        print (temperaturaConvertida)





