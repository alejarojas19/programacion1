#---explicaremos como hacer un grafico en barras---#
import matplotlib.pyplot as plt
lenguajes = ["py","java", "dart", "ts", "elixir"]
encuesta = [50, 10, 20, 10, 10]
plt.bar (lenguajes, encuesta, width= 0.6, color = "m") #---width es para el grosor de las barras---#
###########################
plt.title ("lenguajes mas usados")
plt.xlabel ("lenguajes de programacion")
plt.ylabel ("porcentaje de uso de lenguajes")
plt.savefig ("graficoLenguajes.png")
###########################
plt.show()
