#----entradas----#
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


temperaturaCorporal = [36, 37, 38, 35, 36, 38, 37.5, 38.2, 41,37.4, 38.6,39.1, 40.3, 33]

#----conversiones----#
listaFahrenheit = []
for temperatura in temperaturaCorporal:
    listaFahrenheit.append((temperatura*1.8) + 32)
listaKelvin = []
for temperatura in temperaturaCorporal:
    listaKelvin.append (temperatura + 273.15)


opcionEscogida = float(input (preguntaNumero))

while(opcionEscogida != 4):
    #----opcion1----#
    if(opcionEscogida == 1):
        opcionTemperatura = input(preguntaTemperatura)
        if (opcionTemperatura == "F"):
            print("mostando lista de temperaturas en °F")
            print(listaFahrenheit)
        elif(opcionTemperatura == "K"):
            print("mostrando lista de temperaturas en °K")
            print (listaKelvin)
        elif(opcionTemperatura == "C" ):
            print("no es necesario, la lista ya se muestra en °C")
            print(temperaturaCorporal)
        else:
            print("ingrese una opcion valida")
    
    #----opcion2----#
    elif(opcionEscogida == 2):
        for temperatura  in temperaturaCorporal:
            if (temperatura <= 36):
                print("jmm, la temperatura es baja. El paciente tiene Hipotermia", temperatura)
            elif(temperatura > 36 and temperatura <= 37.5):
                print("temperatura del paciente es normal", temperatura)
            elif(temperatura > 37.5):
                print("la temperatura es alta, el paciente tiene fiebre", temperatura)
            else:
                print("ingresa un rango de temperatura valido")
    
    #----opcion3----#
    elif(opcionEscogida == 3):
        print(mensajeMayor, max(temperaturaCorporal))
        print(mensajeMenor, min(temperaturaCorporal))
        print(mensajeHora, 24/  len(temperaturaCorporal), "horas")
    
    #----opcion no valida----#
    else:
        print("ingresa una opcion valida")
    opcionEscogida = float(input (preguntaNumero))
print("salir del programa")