#Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre
#100, o bien si es divisible entre 400. Puedes hacer la comprobación en esta lista de años bisiestos
#Entrada: 2008 Salida: Es un año bisiesto

año=int(input("Digite el año: "))
if año % 4==0 and año % 400==0:
    print('El año es bisiesto')
else:
    año % 100 != 0
    print('El año no es bisiesto')