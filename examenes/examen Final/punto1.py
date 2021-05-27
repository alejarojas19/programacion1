import matplotlib.pyplot as plt
pregunta_alimento = ("ingresas tus 8 alimentos favotitos : ")
pregunta_precio = ("indica el valor correspondientr a cada alimento elegiodo anteriormente : ")

listaAlimentos = []
for i in range (8):
    alimento  = input(pregunta_alimento)
    listaAlimentos.append(alimento)

listaPrecios = []
for i in range (8):
    precio = float(input(pregunta_precio))
    listaPrecios.append(precio)

plt.bar (listaAlimentos, listaPrecios, width= 0.3, color = "m")
plt.title ("Gráfica  de alimentos favoritos")
plt.xlabel ("alimentos")
plt.ylabel ("precios")
plt.savefig ("AlimentosFavoritos.png")
plt.show()

