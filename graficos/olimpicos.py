#----Medallas de oro en olimpicos de voleibol----#
import matplotlib.pyplot as plt
paises = ["URSS", "Brasil", "EEUU", "Japon", "China", "Cuba", "rusia"]
medallas = [7, 5, 3, 3, 3, 3, 1]
plt.bar (paises, medallas, width= 0.6, color = "c")
plt.title ("medallas de oro en olimpicos")
plt.xlabel ("paises")
plt.ylabel ("Numero de medallas")
plt.savefig ("medallasDeOroEnOlimpicos.png")
plt.show ()
