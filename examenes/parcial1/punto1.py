def sumar (valor1=0, valor2=0, valor3=0):
    suma = valor1+valor2+valor3
    return suma

def restar (valor1=0, valor2=0, valor3=0):
    resta = valor1+valor2+valor3
    return resta

def multiplicar (valor1=0, valor2=0, valor3=0):
    multiplicacion = valor1*valor2*valor3
    return multiplicacion

def dividir (valor1=0, valor2=1, valor3=1):
    division = valor1/valor2/valor3
    return division

def potencia (base=0, valor1=1, valor2=1):
    potenciacion = base ** valor1 ** valor2
    return potenciacion

def operaciones (operacion, valor1, valor2, valor3):
    print (operacion(valor1, valor2, valor3))

operaciones (sumar, 1,2,3)
operaciones (restar, 8,2,1)
operaciones (multiplicar, 6,7,8)
operaciones (dividir,70,3,2)
operaciones (potencia, 4,7,9)
