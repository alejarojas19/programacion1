#---fotopletismografia: (PPG) es una técnica óptica simple usada para descubrir cambios 
#volumétricos en sangre en la circulación periférica
#se utiliza un haz de luz para determinar el volumen de un órgano

import pandas as pd
import matplotlib.pyplot as plt

ppgData = pd.read_csv("ppg.csv", encoding="UTF-8", header=0, delimiter= ";").to_dict()
print(ppgData.keys())
muestras = list (ppgData ["muestra"].values())
print (muestras)
voltaje = list (ppgData ["valor"].values())
print(voltaje)

plt.plot(muestras, voltaje)
plt.title("Grafica fotopletismografia")
plt.xlabel("Tiempo (seg)")
plt.ylabel("Voltaje(mV)")
plt.savefig("fotopletismografia.png")
plt.show()
