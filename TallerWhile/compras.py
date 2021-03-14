VALOR_MONTO = "el monto de una venta es : "
RESPUESTA_ERROR = "ingresa un valor positivo y mayor a cero"
total = 0
monto = float (input ( VALOR_MONTO))

while(monto != 0):
    if (monto < 0):
        print (RESPUESTA_ERROR)
    else:
        total += monto
    monto = float (input (VALOR_MONTO))

if ( total > 1000):
    total -= total*0.1

print ("el monto a pagar es", total)


