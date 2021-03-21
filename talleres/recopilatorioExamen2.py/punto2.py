listaDolares = [20000, 30000, 4000, 2500, 1000, 7600 ]
for elemento in listaDolares:
    if (elemento< 1000):
        print("ingresos bajos")
    elif(elemento > 1000 and elemento < 7000): 
        print ("ingresos medios")
    elif(elemento > 7000 and elemento < 20000):
        print("ingresos altos")
    else:
        print("ingresos elevados")