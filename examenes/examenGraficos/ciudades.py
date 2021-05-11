#Pida a un usuario que ingrese sus 5 ciudades favoritos en el mundo y sus poblaciones luego
#realice un gráfico de torta con la información ingresada y
#resalte la ciudad con mayor población

import matplotlib.pyplot as plt 
pregunta_ciudades = ("hola! ingresa tus 5 ciudades favoritas en el mundo : ")
pregunta_poblacion = ("ingresa sus respectivas poblaciones : ")

ListaCiudades = []
for i in range (5):
    ciudades = input(pregunta_ciudades) #pieLabels
    ListaCiudades.append(ciudades)

ListaPoblacion = []
for i in range(5):
    poblacion = float(input(pregunta_poblacion)) #sizes
    ListaPoblacion.append(poblacion)

maximo = ListaPoblacion.index(max(ListaPoblacion))
pieExplode = [0,0,0,0,0]

pieExplode [maximo]= 0.1

plt.pie(ListaPoblacion, labels=ListaCiudades, explode= pieExplode)
plt.title("Ciudades favoritas")
plt.savefig("Ciudades.png")
plt.show()



