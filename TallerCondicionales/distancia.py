#---- constantes ----#
PREGUNTA_MEDIDA = "ingrese una medida en centimetros : "
PREGUNTA_UNIDAD = """ingrese en que unidades desea transformar : 
K- Kilometros
M- Metros
mm- milimetros
"""
MENSAJE_ERROR = "entrada no valida"

#----entradas----#
medida = float(input(PREGUNTA_MEDIDA))
unidad = input(PREGUNTA_UNIDAD)

#----conversiones----#
metros = medida *10**-2
Kilometros = medida *10**-5
milimetros = medida *10

#----condicionales----#
if(unidad == "K"):
    print(Kilometros)
elif(unidad == "M"):
    print(metros)
elif(unidad == "mm"):
    print(milimetros)
else:
    print (MENSAJE_ERROR)
