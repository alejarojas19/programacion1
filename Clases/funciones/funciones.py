#----------Sumar dos números -----------#
def sumar (a = 0, b = 0):
    '''
        devuelve la suma de dos números a y b
        por defecto A vale cero al igual que B
    '''
    suma = a + b
    return suma

#----------Restar dos números -----------#
def restar (a = 0, b = 0):
    """
        devuelve la resta de dos numeros a y b
        por defecto A vale 0 al igual que B
    """
    resta = a - b
    return resta

#----------Multiplicar dos números -----------#
def multiplicar (a = 0, b = 0):
    """
        devulve la multiplicacion de dos numeros a y b
        por defecto A vale 0 al igual que B
    """
    multiplica = a * b
    return multiplica

#----------dividir dos números -----------#
def dividir (a = 0, b = 1):
    """
        devuelve la division de dos numeros a y b
        por defecto A vale 0 y B vale 1
    """
    dividi = a / b
    return dividi

#----------potenciar dos números -----------#
def potenciar (base = 0, exponente = 1):
    """
        devulve la potencia de dos numeros  base a la exponente
        por defecto la base vale 0 y el exponente 1
    """
    potencia = base ** exponente
    return potencia

#----------funciones dependientes de otras -----------#
def calcular (operacion, numeroA, numeroB):
    print(operacion(numeroA,numeroB))