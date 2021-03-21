import random
canciones = ["cancion1", "cancion2", "cancion3", "cancion4", "cancion5"]

for cancion in (canciones):
    print (cancion)
aleatorio = random.randint(0,4)
print (f'Se seleccionó la siguiente canción: {canciones[aleatorio]}')
