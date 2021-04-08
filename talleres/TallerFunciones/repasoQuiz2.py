temperaturaCorporal = [36, 37, 38, 35, 36, 38, 37.5, 38.2, 41,37.4, 38.6,39.1, 40.3, 33]

#---funciones---#
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
    elif (Preguntatemperatura2 == "F" or Preguntatemperatura2 == "K"):
        print (temperaturaConvertida)
    else:
        print ("ingrese una unidad valida")

def sano (lista):
    temperaturaSaludable = []
    for temperatura in lista:
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

def propiedades (lista):
    print ("la temperatura maxima es", max(lista))
    print ("la temperatura minima es", min(lista))
    print ("la temperatura se tomo cada ", 24/len(lista), "horas")


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

while (entradaMenu > 0 and entradaMenu < 4):
    if (entradaMenu) == 1:
        unidad (temperaturaCorporal)
    elif (entradaMenu) == 2:
        sano (temperaturaCorporal)
    elif (entradaMenu) == 3:
        propiedades (temperaturaCorporal)
    else:
        print ("ingrese una entrada valida")
    entradaMenu = int (input (preguntaNumero))









