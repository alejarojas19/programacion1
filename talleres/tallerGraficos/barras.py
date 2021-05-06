import matplotlib.pyplot as plt
mes = ["enero", "febrero", "marzo", "abril","mayo", "junio"]
ingresos = [200, 150, 400, 120, 500, 350]
plt.bar(mes, ingresos, width= 0.5, color = "c")
plt.title ("Niveles de ingresos")
plt.xlabel ("Mes")
plt.ylabel ("Ingresos")
plt.savefig ("graficoIngresos.png")
plt.show()
