#booleans
pruevaV = True
pruebaF = False
print (pruebaF)
print (pruevaV)
pruebaV = pruebaF
print (pruebaV)
#datos
edad = 19
estatura = 1.72
peso = 65
NOMBRE = "alejandra rojas"
apellido = "rojas"
#preguntar por edad
isMayorEdad = edad >= 18
print ("#"*15, "Mayor Edad", "#"*15)
print (isMayorEdad)
#preguntar por estatura
isMayorEstatura = estatura < 1.70
print ("#"*15, "bajo la estatura promedio", "#"*15)
print (isMayorEstatura)
#preguntar por peso
isPesoDiferente = peso != 65
print ("#"*15, "peso diferente de 65", "#"*15)
print (isPesoDiferente)
#preguntar si el apellido esta en el nombre completo
isApellido = apellido in NOMBRE
print ("#"*15, "esta apellido en el nombre?", "#"*15)
print (isApellido)
#pregunar si la edad es igual
isIgual = 19 == edad
print ("#"*15, "es la misma edad?", "#"*15)
print (isIgual)
