#Escriba un programa en Python que acepte una cadena de texto e indique si todos sus caracteres son alfabéticos
contar=0
texto=input("Digite el texto: ")
alfabeto='aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVxXyYzZ'

for i in texto:
    if i in alfabeto:
        contar+=1
    else:
        print("Se ha encontrado caracteres No alfabeticos")
    break
if contar==len(texto):
    print("Todos los caracteres son alfabeticos")        