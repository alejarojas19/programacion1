class Estudiante ():
    """ Esta es la clase estudiante y aquí se conocerá
        la edad de estudiante
        su nombre
        # de identificacion
        carrera que estudia
        semestre que cursa
        Además, se muestra el tiempo en pantalla que estudia 
        """
    
    def __init__ (self, edadEntrada, nombreEntrada, identificacionEntrada, carreraEntrada, semestraEntrada):
        print ("Hola soy un estudiante nuevo")
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.identificacion = identificacionEntrada
        self.carrera = carreraEntrada
        self.semestre = semestraEntrada
    
    def atributos (self):
        print (f"""Hola mi nombre es {self.nombre}, mi ID es {self.identificacion}
                tengo {self.edad}
                estoy estudiando {self.carrera} y voy en {self.semestre} semestre, espero terminar rapido
                """)
    
    def tiempoEstudiando (self, materiaEntrada, horasEntrada):
        self.materia = materiaEntrada
        self.horas = horasEntrada
        print (f"soy {self.nombre} y estudiaré {self.materia} por {self.horas} horas, espero me rinda")

estudiante1 = Estudiante (19, "Alejandra", 1000203837, "Ingenieria Biomedica", 4)
estudiante2 = Estudiante (22, "juan Manuel", 1039473803, "fisioterapia", 9)

estudiante1.atributos()
estudiante2.atributos()
estudiante1.tiempoEstudiando ("anatomía", 3)
estudiante2.tiempoEstudiando ("nuerología", 5)