temperaturaCorporal = [36, 37, 38, 35, 36, 38, 37.5, 38.2, 41, 37.4, 38.6, 39.1, 40.3, 33]
mensajeMayor = "La temperatura mas alta es --> "
mensajeMenor = "La temperatura mas baja es --> "
mensajeHora = "La temperatura se tomo cada"

print(mensajeMayor, max(temperaturaCorporal))
print(mensajeMenor, min(temperaturaCorporal))
print(mensajeHora, 24/  len(temperaturaCorporal), "horas")
