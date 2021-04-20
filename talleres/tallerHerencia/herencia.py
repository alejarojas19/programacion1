class Persona ():
    """ esta es la clase persona, aca se encontrara:
        el nombre
        numero de identificación
        edad
        Ademas dado unn mensaje la persona habla 
        y muestra la cantidad de pasos  que ha dado la persona
        """
    
    def __init__ (self, entradaNombre, entradaID, entradaEdad):
        print("Hola soy una nueva persona")
        self.nombre = entradaNombre
        self.identificacion = entradaID
        self.edad = entradaEdad
    
    def hablar (self, mensaje):
        print (f"hola me llamo {self.nombre}, vengo a traerte un mensaje... {mensaje}")
    
    def caminar (self, pasos):
        for i in range (pasos):
            print (f"hola soy {self.nombre} me gusta caminar y hoy he dado {i+1} paos")

aleja = Persona ("Alejandra", 1000203837, 19)
aleja.hablar ("amo los animales y quiero tener muchos perros")
aleja.caminar (9)
print ("♦"*50)

#------Doctor------#
class Doctor (Persona):
    def __init__ (self, entradaNombre, entradaID, entradaEdad, entradaEspecialidad):
        Persona.__init__(self, entradaNombre, entradaID, entradaEdad)
        self.especialidad = entradaEspecialidad
    
    def tratamineto (self, enfermedad):
        print (f"""Hola soy el doctor {self.nombre}, soy especialista en {self.especialidad}
                y voy a tratar tu enfermedad, no te austes hay muchos tratamientos para 
                tartar tu {enfermedad}""")

juan = Doctor ("Juan Carlos", 43555825, 46, "dermatologia")
juan.tratamineto("melanoma")
print ("♦"*50)

#------Nutricionista------#
class Nutricionista (Persona):
    def __init__ (self, entradaNombre, entradaID, entradaEdad, entradaUniverdidad):
        Persona.__init__(self, entradaNombre, entradaID, entradaEdad,)
        self.universidad = entradaUniverdidad
    
    def IMC (self, entradaPeso, entradaAltura):
        self.peso = entradaPeso
        self.altura = entradaAltura
        IMC = self.peso / (self.altura**2)
        print (f"""Hola mi nombre es {self.nombre}
                    soy nutricionista de la universidad {self.universidad}.
                    Hoy vengo a darte el resultado de un examen, el cual fue con los
                    datos que diste, que son tu peso {self.peso} Kilogramos y tu altura {self.altura} centimetros
                    El resultado de tu indice de masa corporal es {IMC}
                    """)

sebastian = Nutricionista("Sebastian", 98522095, 53, "CES")
sebastian.IMC (70, 1.77)
print ("♦"*50)

#------Abogado------#
class Abogado (Persona):
    def __init__ (self, entradaNombre, entradaID, entradaEdad, entradaEspecialidad, entradaUniverdidad):
        Persona.__init__(self, entradaNombre, entradaID, entradaEdad)
        self.universidad = entradaUniverdidad
        self.especialidad = entradaEspecialidad
    
    def representante (self, nombreCliente, entradaCaso):
        self.cliente = nombreCliente
        self.caso = entradaCaso
        print (f"""Hola mi nombre es {self.nombre}, soy abogado especialista en {self.especialidad}
                graduado de la {self.universidad}. Procedo a representar a {self.cliente} en el caso de {self.caso}
                """)

diego = Abogado ("Diego Carvajal", 43678432, 50, "derecho penal", "Universidad de Los Andes")
diego.representante("sofia", "Robo de un banco")
print ("♦"*50)