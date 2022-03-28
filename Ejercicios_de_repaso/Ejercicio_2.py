#Escriba un programa en Python que acepte una cadena de texto e indique si todos sus caracteres son alfabéticos
contar=0
Alfabeto=('aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVxXyYzZ')
Texto=input('Digite la palabra: ')

for i in Texto:
    if Texto in Alfabeto:
        contar+=1        
else:
    print("Se ha encontrado caracteres No alfabeticos")
    
if contar==len(Texto):
    print("Todos los caracteres son alfabeticos")        