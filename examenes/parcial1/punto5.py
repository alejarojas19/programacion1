def patron (posicion):
    a = 0
    b = 1
    for elemento in range (posicion -1):
        c = a + b
        a = b
        b = c
    return (a)

numero = patron (5)
print ("el nuemro que corresponde con la sucesion es",numero)