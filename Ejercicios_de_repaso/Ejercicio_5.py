#Escriba un programa en Python que acepte dos valores enteros (𝑥 e 𝑦) que
#representarán un punto (objetivo) en el plano. El programa simulará el movimiento de
#un «caballo» de ajedrez moviéndose de forma alterna: 2 posiciones en 𝑥 + 1 posición en
#𝑦. El siguiente movimiento que toque sería para moverse 1 posición en 𝑥 + 2 posiciones
#en 𝑦. El programa deberá ir mostrando los puntos por los que va pasando el «caballo»
#hasta llegar al punto objetivo
x=int(input('Digite el numero: '))
y=int(input('Digite el numero: '))
for x in range(0,1):
    for y in range(0,1):
        print(f'({x},{y})', end=',')
        x+=1
        y+=2
        print(f'({x},{y})', end=',')
        x+=2
        y+=1
        print(f'({x},{y})', end=',')
        x+=1
        y+=2
        print(f'({x},{y})', end=',')
        x+=2
        y+=1
        print(f'({x},{y})', end=',')
        x+=1
        y+=2
        print(f'({x},{y})', end=',')