#Escriba un programa en Python que pida (por separado) dos valores numéricos y un operando
#(suma, resta, multiplicación, división) y calcule el resultado de la operación, usando para ello
#la sentencia match-case
numero1=int(input('Digite un valor: '))
numero2=int(input('Digite un valor: '))

match numero1,numero2:
    case 