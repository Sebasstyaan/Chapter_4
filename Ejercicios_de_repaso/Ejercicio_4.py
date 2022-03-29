#Escriba un programa en Python que acepte dos cadenas de texto y compute el producto
#artesiano letra a letra entre ellas
primero=input('Digite letras: ')
segundo=input('Digite numeros: ')
for letra in primero:
    for numero in segundo:
        print(f'{letra}{numero}', end=',')