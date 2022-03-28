#Escriba un programa en Python que acepte un país (como «string») y muestre por
#pantalla su bandera (como «emoji»). Puede restringirlo a un conjunto limitado de países
pais=(input('digite el nombre del pais: '))

if pais=='Italia':
    bandera='🇮🇹'
    print(f'bandera: {bandera}')
elif pais=='Suecia':
    bandera='🇸🇪'
    print(f'bandera: {bandera}')
elif pais=='Estados unidos':
    bandera='🇺🇸'
    print(f'bandera: {bandera}')
elif pais=='España':
    bandera='🇪🇸'
    print(f'bandera: {bandera}')
elif pais=='China':
    bandera='🇨🇳'
    print(f'bandera: {bandera}')
elif pais=='Brazil':
    bandera='🇧🇷'
    print(f'bandera: {bandera}')
else:
    print(f'bandera de pais no encontrada: 🚩')