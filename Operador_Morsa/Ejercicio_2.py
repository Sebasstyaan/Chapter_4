a1=int(input("digite el primer numero: "))
a2=int(input("digite el segundo numero : "))
a3=int(input("digite el tercer numero : "))

if a1<a2<a3 or a1<a3<a2:
    print(f"el numero menor es: {a1}")
elif a2<a1<a3 or a2<a3<a1:
    print(f"El numero menor es: {a2}")
elif a3<a2<a1 or a3<a1<a2:
    print(f"El numero menor es: {a3}")
elif a1==a2  a1<a3:
    print(f"Se digitaron 2 numeros iguales:numero1={a1} numero2={a2}")
elif a1==a3:
    print(f"Se digitaron 2 numeros iguales:numero1={a1} numero3={a3}")
elif a2==a3:
    print(f"Se digitaron 2 numeros iguales:numero2={a2} numero3={a3}")
else:
    print("Los 3 numeros digitados son iguales")