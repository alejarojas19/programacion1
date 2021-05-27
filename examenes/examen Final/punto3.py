def validatefloat (pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = float (input(pregunta))
            isCorrectData = True
        except ValueError:
            print ("los datos que ingresaste no son correctos, intenta nuevamente")
        return valor

def validateString (pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = input(pregunta)
            assert(valor.isalpha())
            isCorrectData = True
        except AssertionError:
            print ("los datos que ingresaste no son correctos, intenta nuevamente")
        return valor

def pedirDatos ():
    preguntaNombre = "hola! ingresa tu nombre : "
    preguntaDolar = "ingresa la cantida de dolares que tienes para convertirlos a euros : "
    nombre = validateString(preguntaNombre)
    dolares = validatefloat(preguntaDolar)
    return nombre, dolares

def calcularEuros ():
    nombreEntrada, dolaresEntrada = pedirDatos()
    euros = dolaresEntrada*0.82
    print (f"la cantidad de dolares que tienes pasada a euros es de {euros}")
    return euros

calcularEuros ()

