import matplotlib.pyplot as plt
pieLabels = ["Bogota", "Medellin", "Cali", "Barranquilla"] #Etiquetas
sizes = [10.4,2.5, 2.4, 1.2] #Tamaño de cada porcion de torta
pieExplode = [0.1, 0, 0, 0] #que tan alejado esta del origen

def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento
    for i in range (len(labels)):
        porccentaje = round(sizes[i]/acumulador*100, 2)
        pieLabels[i] += indicador+str(porccentaje) +' Millones de Habitantes'

etiquetarElementosPorcentuales(sizes, pieLabels,'*')

plt.pie(sizes,labels=pieLabels, explode=pieExplode, shadow= True, counterclock = True, startangle= 45)
plt.title('Ciudades de colombia --> porcentaje: millones de habitantes')
plt.savefig('pieCiudades.png')
plt.show()