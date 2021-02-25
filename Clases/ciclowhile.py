#----mensajes----#
MENSAJE_SALUDAR = "hola, como estas"
MENSAJE_AHORRO = "llevas ahorrado"
PREGUNTAR_VALOR = "cuanto vale el pc que deseas? : "
PREGUNTAR_CUANTO_TIENE = "cuanto llevas ahorrado? : "

#----entradas----#
print(MENSAJE_SALUDAR)
valor = float(input(PREGUNTAR_VALOR))
ahorrado = float(input(PREGUNTAR_CUANTO_TIENE))

while(valor > ahorrado): 
    print(MENSAJE_AHORRO, ahorrado, "te faltan...", valor - ahorrado)
    ahorrado = ahorrado +1000
print(valor == ahorrado)