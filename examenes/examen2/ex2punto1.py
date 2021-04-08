temperaturaCorporal = [36, 37, 38, 35, 36, 38, 37.5, 38.2, 41,37.4, 38.6,39.1, 40.3, 33]

preguntaTemperatura = """
                        F- fahrenheit (°F)
                        K- kelvin (°K)
                        C- celcius (°C)
"""
listaFahrenheit = []
for temperatura in temperaturaCorporal:
    listaFahrenheit.append((temperatura*1.8) + 32)
listaKelvin = []
for temperatura in temperaturaCorporal:
    listaKelvin.append (temperatura + 273.15)

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