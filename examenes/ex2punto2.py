temperaturaCorporal = [36, 37, 38, 35, 36, 38, 37.5, 38.2, 41,37.4, 38.6,39.1, 40.3, 33]

for temperatura  in temperaturaCorporal:
    if (temperatura <= 36):
        print("jmm, la temperatura es baja. El paciente tiene Hipotermia", temperatura)
    elif(temperatura > 36 and temperatura <= 37.5):
        print("temperatura del paciente es normal", temperatura)
    elif(temperatura > 37.5):
        print("la temperatura es alta, el paciente tiene fiebre", temperatura)
    else:
        print("ingresa un rango de temperatura valido")