class Canguro ():
    """Esta es la clase canguro, aqui encontraras su nombre,
        su edad y su ID. Ademas, muestra la cantidad de salto que ha dado
    """
    def __init__ (self, entradaNombre, entradaEdad, entradaID):
        print ("hola soy un canguro nuevo")
        self.nombre = entradaNombre
        self.edad = entradaEdad
        self.identificacion = entradaID
    
    def saltos (self, numeroSaltos):
        for i in range (numeroSaltos):
            print(f'Hola mi nombre es {self.nombre}, soy un canguro y  amo saltar. Hoy he dadoo {i+1} saltos')



canguro1 = Canguro ("matias", 4, 1000324657)
canguro1.saltos(7)