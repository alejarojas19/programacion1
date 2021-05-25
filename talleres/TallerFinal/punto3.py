def validateFloat (pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = float (input(pregunta))
            isCorrectData = True
        except ValueError:
            print ("datos incorrectos, ingresalos nuevamente")
        return valor

def validateString (pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = input(pregunta)
            assert(valor.isalpha())
            isCorrectData = True
        except AssertionError:
            print ("datos incorrectos, ingresalos nuevamente")
        return valor

def validarArchivo(nombreArchivo, descripcion):
    try:
        archivo = open(nombreArchivo)
        return True
    except FileNotFoundError:
        archivo = open(nombreArchivo, 'w', encoding='UTF-8')
        print("2")
        archivo.writelines(descripcion)
        return False

def guardarLinea (nombreArchivo, lineaIn):
    archivo = open(nombreArchivo,'a')
    archivo.writelines(lineaIn)

nameFile = "mantenimientos.txt"
isValidate = validarArchivo(nameFile, 'Seguimiento de mantenimiento de equipos medicos')
if (isValidate):
    descEquipo = input('Ingrese la descripción del equipo : ')
    nombre = validateString('Ingrese su nombre :')
    precio = validateFloat('Ingrese el precio : ')
    linea ='\nDescripcion465'+ descEquipo+ ' nombre técnico: ' + nombre + ' precio acordado: '+ str(precio)
    guardarLinea(nameFile, linea)
else:
    print('se creó el archivo')