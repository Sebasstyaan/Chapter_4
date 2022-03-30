#Escriba un programa en Python que acepte dos valores enteros (𝑥 e 𝑦) que
#representarán un punto (objetivo) en el plano. El programa simulará el movimiento de
#un «caballo» de ajedrez moviéndose de forma alterna: 2 posiciones en 𝑥 + 1 posición en
#𝑦. El siguiente movimiento que toque sería para moverse 1 posición en 𝑥 + 2 posiciones
#en 𝑦. El programa deberá ir mostrando los puntos por los que va pasando el «caballo»
#hasta llegar al punto objetivo
x=int(input('Digite el numero: '))
y=int(input('Digite el numero: '))
p1=0
p2=0
flujo=True
while p1!=x and p2!=y:
    if flujo:
        p1+=1
        p2+=2
        print(f'({p1}.{p2})', end=',')
    else:
        p1+=2
        p2+=1
        print(f'({p1}.{p2})', end=',')
        #flujo=not flujo