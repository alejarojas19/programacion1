import matplotlib.pyplot as plt

#---creamos los Labels sizes y explode---#

pieLabels = ["python", "java", "dart", "js"] #Etiquetas
sizes = [45, 30, 15, 10] #Tamaño de cada porcion de torta
pieExplode = [0, 0, 0.1, 0] #que tan alejado esta del origen

#----Diferentes formas----#

#Grafica sin etiquetas, solo divisiones
plt.pie(sizes)
plt.title('Uso de lenguajes de programación en el 2021 --> solo divisiones')
plt.savefig('tortasLenguajes1.png')
plt.show()

#grafica con etiquetas y divisiones
plt.pie(sizes,labels=pieLabels)
plt.title('Uso de lenguajes de programación en el 2021 --> etiquetas')
plt.savefig('tortasLenguajes2.png')
plt.show()

#grafica alejada del origen
pieExplode = [0, 0, 0.1, 0]
plt.pie(sizes,labels=pieLabels, explode=pieExplode)
plt.title('Uso de lenguajes de programación en el 2021 --> alejada del origen')
plt.savefig('tortasLenguajes3.png')
plt.show()

#grafica con sombra
pieExplode = [0, 0, 0.2, 0]
plt.pie(sizes,labels=pieLabels, explode=pieExplode, shadow= True)
plt.title('Uso de lenguajes de programación en el 2021 --> con sombra')
plt.savefig('tortasLenguajes4.png')
plt.show()

#grafica con cambio de angulo de inicio
pieExplode = [0, 0, 0, 0.3]
plt.pie(sizes,labels=pieLabels, explode=pieExplode, shadow= True, startangle= 45)
plt.title('Uso de lenguajes de programación en el 2021 --> cambio de angulo')
plt.savefig('tortasLenguajes5.png')
plt.show()

#grafica que muestra el porcentaje de cada elemento 
def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento
    for i in range (len(labels)):
        pieLabels[i] += indicador+str(sizes[i]/acumulador*100) +'%'

etiquetarElementosPorcentuales(sizes, pieLabels,'☺')

plt.pie(sizes,labels=pieLabels, explode=pieExplode, shadow= True, counterclock = True, startangle= 45)
plt.title('Uso de lenguajes de programación en el 2021 --> porcentaje en cada elemento')
plt.savefig('tortasLenguajes6.png')
plt.show()