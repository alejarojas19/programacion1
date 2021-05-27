class Humano ():
    """ 
        Esta es la clase humano, aca podras ver atributos como
        nombre, sexo, edad. Posteriormente tiene la accion de 
        hablar
    """
    def __init__(self, entranaNombre, entradaSexo, entradaEdad):
        print("Hola, soy un humano")
        self.nombre = entranaNombre
        self.sexo = entradaSexo
        self.edad = entradaEdad
    def hablar (self, mensaje):
        print( f"hola, soy {self.nombre}, me gusta programacion y estoy en clase con el mejor profesor, no quiero que se vaya")
    def mostrarAtributos (self):
        print (f"hola mi nombre es {self.nombre}, soy de sexo {self.sexo}, tengo {self.edad} y vengo a traerte un mensaje")

humano1 = Humano("Alejandra", "femenino", 19)
humano1.hablar("hola, espero estes muy bien")
humano1.mostrarAtributos

#----Doctor----#
class Doctor (Humano):
    def __init__(self, entranaNombre, entradaSexo, entradaEdad):
        super().__init__(entranaNombre, entradaSexo, entradaEdad)
    def imc (self, entradaPeso, entradaEstatura):
        self.peso = entradaPeso
        self.Estatura = entradaEstatura
        imc = self.peso / (self.Estatura)**2
        print (f"hola soy  el doctor {self.nombre}, tu indice de masa corporal es {imc}")

doctor1 = Doctor("Juan Manuel", "masculino", 22)
doctor1.imc(70, 1.77)