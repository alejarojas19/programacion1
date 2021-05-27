def validarArchivo(nombreArchivo):
    try:
        archivo = open(nombreArchivo)
        return True
    except FileNotFoundError:
        archivo = open(nombreArchivo, 'w', encoding='UTF-8')
    return False

def guardarLinea (nombreArchivo, lineaIn):
    archivo = open(nombreArchivo,'a')
    archivo.writelines(lineaIn)

nombreArchivo = "pacientes.txt"
isValidate = validarArchivo(nombreArchivo)
if (isValidate):
    nombre = input ("ingresa el nombre del paciente : ")
    enfermedad = input ("añade la descripcion de la enfermedad del paciente ingresado : ")
    precio = float(input("ingresa el precio de la consulta : "))
    linea = "\ndescripcion : " + enfermedad + " nombre del paciente : " + nombre + " precio consulta : " + str(precio)
    guardarLinea(nombreArchivo, linea)
else:
    print ("se creo el archivo")

