import matplotlib.pyplot as plt

tiempo = [0,1,2,3,4,5]
sensor = [4,5,6,8,9,10]
plt.plot(tiempo,sensor, "--", "c")
#############################
plt.title("grafico sensor contra el tiempo")
plt.xlabel("tiempor (s)")
plt.ylabel ("voltaje (mV)")
plt.savefig("sensor.png")
#############################
plt.show()

#----diccionarios----#
diccionario = {}
diccionario ["nombresEstudiantes"] = ["jacobo", "daniel", "maria", "elena"]
diccionario ["edadEstudiantes"] = [18, 17, 24, 32]
diccionario ["peso"] = [84, 56, 64, 57]
print(diccionario)
print(diccionario["nombresEstudiantes"][-1], diccionario["edadEstudiantes"][-1], diccionario["peso"][-1])


