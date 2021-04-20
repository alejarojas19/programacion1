class Nuutricionista ():
    """ Esta es la clase nutricionista, se mostrara
        la edad, el nomnre y la universidad
        de donde se graduo el profesional.
        Además, clacula el IMC del paciente
        """
    
    def __init__ (self, entradaNombre, entradaEdad, entradaUniversidad):
        print ("Hola, soy un nutricionista")
        self.nombre = entradaNombre
        self.edad = entradaEdad
        self.universidad = entradaUniversidad
    
    def masaCorporal (self, pesoEntrada, alturaEntrada):
        self.peso = pesoEntrada
        self.altura = alturaEntrada
        IMC = self.peso / (self.altura **2)
        print (f"""Hola soy tu nuticionista, mi nombre es {self.nombre} tengo {self.edad}
                y me gradue de la universidad {self.universidad}. Calcule tu indice de masa corporal,
                con tu peso {self.peso} y tu altura {self.altura}, dando como resultado de tu IMC {IMC}
                """)

nutricionista1 = Nuutricionista ("Manuela", 25, "CES")
nutricionista1.masaCorporal (65, 1.74)
