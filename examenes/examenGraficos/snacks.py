#Pida a un usuario que ingrese sus 5 snacks favoritos y sus precios luego realice un gráfico de 
#barras con la información ingresada

import matplotlib.pyplot as plt 
pregunta_snaks = ("hola! ingresa tus 5 snacks favortios: ")
pregunta_precio = ("ingresa el valor correspondiente a cada snack que ingresaste: ")

ListaSnacks = []
for i in range(5):
    snack = input(pregunta_snaks)
    ListaSnacks.append(snack)

ListaPrecios = []
for i in range(5):
    precio = int(input(pregunta_precio))
    ListaPrecios.append(precio)

plt.bar (ListaSnacks, ListaPrecios, width= 0.5, color= "c")
plt.title("Snacks favoritos")
plt.xlabel("snakcs")
plt.ylabel("precios")
plt.savefig("snakcs.png")
plt.show()

