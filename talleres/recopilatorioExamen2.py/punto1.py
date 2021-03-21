listaDolares = [20000, 30000, 4000, 2500, 1000, 7600 ]

preguntaMoneda = """
                    C- mostar lista en pesos
                    D- mostar lista original en dolares
                    E- mostar lista en euros
"""
listaPesos = []
for elemento in listaDolares:
    listaPesos.append(elemento*3700 )
listaEuros = []
for elemento in listaDolares:
    listaEuros.append(elemento* 0.84)

opcionMoneda = input(preguntaMoneda)
if (opcionMoneda == "C"):
    print("mostarndo lista en pesos")
    print(listaPesos)
elif (opcionMoneda == "D"):
    print("mostarndo lista original")
    print(listaDolares)
elif (opcionMoneda == "E"):
    print("mostrando lista en euros")
    print(listaEuros)
else:
    print ("ingrese una opcion valida")