#----Izavella Valencia----Elsa Guenet----Alejandra Rojas----#

#----punto1----#
class ElementoDigital ():
    """Esta es la clase Elemento Digital, muestra en pantalla
        las generalidades de la canción como 
        nombre
        creador
        fecha de publicación
        Ademas, al final muestra todos sus atributos
        """
    
    def __init__ (self,entradaNombre, entradaFecha, entradaCreador):
        print ("Esta es una nueva cancion, espero la disfrutes")
        self.nombre = entradaNombre
        self.fecha = entradaFecha
        self.creador = entradaCreador
    
    def atributos (self):
        print (f""" Esta cancion se llama {self.nombre} ,
            fue creada en {self.fecha} y 
            su creador es {self.creador}
            """)

spotify = ElementoDigital ("spotify","abril 2006", "Daniel Ek")
spotify.atributos()
print("*"*50)

#----punto2----#
class Usuario ():
    """Esta es la clase usuario, mostrara en pantalla
        nombre
        edad
        sexo
        nacionalidad
        Al final muestra sus atributos
        """
    def __init__(self, entradaNombre, entradaEdad, entradaSexo, entradaNacionalidad):
        self.nombre = entradaNombre
        self.edad = entradaEdad
        self.sexo = entradaSexo
        self.nacionalidad = entradaNacionalidad
    def atributos (self):
        print (f'''El nombre del usuario es {self.nombre}
        El usuario tiene una edad de {self.edad} años
        El sexo del usuario es {self.sexo}
        La nacionalidad del usuario es {self.nacionalidad}
        ''')
usua = Usuario ('Alejandra Rojas', 19, 'femenino', 'Francesa')
usua.atributos()
print("*"*50)

#----punto3----#
class Pagina ():
    """Esta es la clase pagina, muestra en la pantalla 
        Tipo de contenido 
        Formato 
        Fecha de publicacion
        """ 
    def __init__ (self,entradaContenido, entradaFormato, entradaFecha):
        self.contenido = entradaContenido
        self.Formato = entradaFormato
        self.Fecha = entradaFecha
    def atributos (self):
        print(f"""El tipo de contenido de esta pagina es {self.contenido}
                el formato es {self.Formato}
                la fecha de publicacion es {self.Fecha}
                """)

pagina1 = Pagina ("musicaL", "OGG", "abril 2006")
pagina1.atributos()
print("*"*50)

#-----------------------Herencia-----------------------#

#----punto1----#
class Cancion (ElementoDigital):
    def __init__ (self,entradaNombre, entradaFecha, entradaCreador, entradaGenero, entradaDuracion):
        ElementoDigital.__init__(self,entradaNombre, entradaFecha, entradaCreador)
        self.genero = entradaGenero
        self.duracion = entradaDuracion
        print(f"Esta es un nueva cancion que se llama {self.nombre} y fue creada en {self.fecha}")
    def reproducciones (self, numeroReproducciones):
        for i in range (numeroReproducciones):
            print (f"{self.nombre} sonando {i+1} vez")

cancion2 = Cancion("Baby", "junio 2012", "Justin Bieber", "pop", "3 minutos")
cancion2.reproducciones (5)
print("*"*50)

#----punto2----#
class Artista (Usuario):
    def __init__(self, entradaNombre, entradaEdad, entradaSexo, entradaNacionalidad, entradaGenero, entradaNumero, entradaAlbums, entradaCiudad):
        Usuario.__init__(self, entradaNombre, entradaEdad, entradaSexo, entradaNacionalidad)
        self.genero = entradaGenero
        self.numero = entradaNumero
        self.albums = entradaAlbums
        self.ciudad = entradaCiudad
        print (f'El conciento se dara en la ciudad de {self.ciudad}')
    def atributos(self):
        print (f'''El genero musical que canta el artista es {self.genero}
        El numero de canciones publicadas es {self.numero}
        Este artista tiene un total de {self.albums} albums
        ''')
artista1 = Artista('Alejandra Rojas', 19, 'femenino', 'Francesa', 'reggaeton', 50, 5, 'España')
artista1.atributos()
print("*"*50)

#----punto3----#
class Favoritos (Pagina):
    def __init__ (self,entradaContenido, entradaFormato, entradaFecha, entradaFavoritos, entradaFechaActualizacion):
        Pagina.__init__(self, entradaContenido, entradaFormato, entradaFecha)
        self.favoritos = entradaFavoritos
        self.fechaActualizacion = entradaFechaActualizacion
    def cancionNueva (self, cancion, actualizacion):
        self.favoritos.append(cancion)
        self.fechaActualizacion = actualizacion
    def eliminarElemento (self, cancionEliminada):
        print (self.favoritos)
        self.favoritos.pop(cancionEliminada)
favortias1 = ["bichota","tusa", "DVD","fiel", "makinon"]
spotify1 = Favoritos ("cancion","OGG", "octubre 2006",favortias1, 2021)
spotify1.eliminarElemento(4)
spotify1.cancionNueva ("leyendas", 2021)
print(spotify1.favoritos)


