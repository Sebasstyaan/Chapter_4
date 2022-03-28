#Escriba un programa en Python que realice las siguientes 9 multiplicaciones.
Numero=input('Digite el numero: ')

for i in range(1,10):
    valor=int(Numero*i)
    resultado=valor*valor
    print(f'{valor} . {valor} = {resultado}')