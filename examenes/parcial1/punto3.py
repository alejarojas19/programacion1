preguntaBase = int(input("ingrese la medida de la base : "))
preguntaAltura = int(input("ingrese la medida de la altura : "))

def area (preguntaBase, preguntaAltura):
    areaTriangrulo = (preguntaBase * preguntaAltura)/2
    return areaTriangrulo

print ("el area del triangulo es", area(preguntaBase,preguntaAltura))