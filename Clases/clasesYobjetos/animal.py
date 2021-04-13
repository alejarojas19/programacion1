class Perro ():
    """
        Esta es la clase Perro, el mejor ser vivo que 
        puede existir. Aquí veras los siguientes atributos 
        que diferencian a un peludo de otro:
        entradaNombre --> hace referencia al nombre del bebe
        entradaEdad --> indica cuantos años felices tiene
        entradaPeso --> hace referencia a los kilos de amor
        entradaSexo --> indica si es macho o hembra
        Además, tiene las siguientes acciones que lo hacen unico:
        *saludo (accion):
            al llegar su amo describe como lo saluda
        *mostrarAtributos ():
            mustra los atributos por los cuales es unico 
        *actividadFav ():
            dice su actividad favorita en el dia 
    """
    def __init__ (self, nombreEntrada, edadEntrada, pesoEntrada, sexoEntrada):
        print ("Hola, soy un perro nuevo y vengo a llenarte de amor")
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.peso = pesoEntrada
        self.sexo = sexoEntrada
    
    def saludar (self):
        print (f"hola soy {self.nombre} cuando llegas muevo mucho la cola, me tiro al piso para que me sobes la barriga y siempre reclamo mi galleta como premio")
    
    def mostrarAtributos (self):
        print (f""" mi nomre es {self.nombre}
                tengo {self.edad} años de ser muy feliz
                peso {self.peso} kilos, estoy rellenito de amor
                soy un {self.sexo}
        """)
    
    def actividadFav (self):
        print (f"me llamo {self.nombre} lo que mas me gusta hacer es dormir, me encanta que me mimen, me gusta salir a caminar y que me den galletas")


perro1 = Perro ("Robin", 8, 6, "macho")
perro2 = Perro ("manchas", 9, 10, "macho")
perro3 = Perro ("lupe", 4, 6, "hembra")

perro3.saludar()
perro2.mostrarAtributos()
perro1.actividadFav()
