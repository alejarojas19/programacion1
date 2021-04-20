class Piano ():
    """Esta es la clase piano, es un intrumento musical 
        que representa elegancia. Aquí encontraras
        sus principales caracteristicas
    """
    def __init__ (self, tipoEntrada, colorEntrada, añosEntrada):
        self.tipo = tipoEntrada
        self.color = colorEntrada
        self.años = añosEntrada
    
    def cancion (self, cancion):
        print (f"estan tocando la cancion {cancion} en el piano")

piano1 = Piano ("electirco", "negro", 5)
piano1.cancion("Diamonds")