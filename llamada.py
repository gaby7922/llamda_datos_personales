# calcula el costo de llamada
minuto = 11
costo = 100 * minuto
#cuando pasan de 11 minutos
if minuto >= 11:
    costo += (costo * 0.05) 
    print ("La tarifa a pagar es: " , costo)
#cuando es menos de 10 minutos
else:
    print ("la tarifa a pagar es: ", costo)

    
