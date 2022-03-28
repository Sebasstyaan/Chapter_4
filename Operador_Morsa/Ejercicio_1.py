jugador1=input("Digite su opcion jugador1: ")
jugador2=input("Digite su opcion jugador2: ")
if jugador1==jugador2:
    print(f'Han empatado')
elif jugador1=="papel" and jugador2=="tijera":
    print("Ha Ganado el jugador2: la tijera corta el papel")
elif jugador1=="papel" and jugador2=="piedra":
    print("Ha Ganado el jugador1: el papel envuelve la piedra")
elif jugador1=="tijera" and jugador2=="papel":
    print("Ha Ganado el jugador1: la tijera corta el papel")
elif jugador1=="tijera" and jugador2=="piedra":
    print("Ha Ganado el jugador2: la piedra aplasta la tijera")
elif jugador1=="piedra" and jugador2=="tijera":
    print("Ha Ganado el jugador1: la piedra aplasta la tijera")
elif jugador1=="piedra" and jugador2=="papel":
    print("Ha Ganado el jugador2: el papel en vuelve la piedra")