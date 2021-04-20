class Torta ():
    """ Esta es la clase Torta y muestra 
        su forma
        su sabor
        su altura
        Además, tiene una funcion que muestra todos sus atributos
    """
    def __init__ (self, formaEntrada, saborEntrada, alturaEntrada):
        print ("hola, soy una deliciosa torta")
        self.forma = formaEntrada
        self.sabor = saborEntrada
        self.altura = alturaEntrada
    
    def mostrarAtributos (self):
        print (f""" hola soy una rica torta en forma de {self.forma}
            mi sabor que me diferencia de las demas es {self.sabor} 
            y mi altura es de {self.altura} centímetros
            ¡disfrútame!""")

torta1 = Torta ("cuadrado", "chocolate", 12)
torta2 = Torta ("circular", "fresa", 20)

torta1.mostrarAtributos()
torta2.mostrarAtributos()

