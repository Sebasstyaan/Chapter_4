#Escriba un programa en Python que acepte edad, peso, pulso y plaquetas, y determine
#si una persona cumple con estos requisitos para donar sangre.
Edad=int(input("Digite su edad: "))
peso=int(float(input("Digite su peso: ")))
latidos=int(input("Digite sus latidos de corazon por minuto: "))
plaquetas=int(float(input("Digite la cantidad normal de plaquetas: ")))

if Edad>18 and Edad<50:
    peso>50 and peso<85
    latidos>65 and latidos<100
    plaquetas>150000
    print("¡Apto! para donar sangre")
else:
    print("¡No! es apto para donar sangre")