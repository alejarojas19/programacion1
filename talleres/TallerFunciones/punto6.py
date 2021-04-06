peso = float(input("ingrese su peso :"))
altura = float(input("ingrese su altura :"))

def calcularIMC (peso, altura):
    return round (peso / altura **2)

print (calcularIMC (peso, altura))
