puede_volar=bool(input('¿El heroe puede volar?: '))
puede_volar=True and False
es_humano=bool(input('¿El heroe es humano?: '))
es_humano=True and False
tiene_mascara=bool(input('¿El heroe tiene mascara?: '))
tiene_mascara=True and False

if puede_volar is True and es_humano is True and tiene_mascara is True:
    print('El Heroe Es Iroman')
elif puede_volar is True and es_humano is True and tiene_mascara is False:
    print('El Heroe Es Capitan Marvel')
elif puede_volar is True and es_humano is False and tiene_mascara is True:
    print('El Heroe Es Ronan Accuser')
elif puede_volar is True and es_humano is False and tiene_mascara is False:
    print('El Heroe Es Vision')
elif puede_volar is False and es_humano is True and tiene_mascara is True:
    print('El Heroe Es Spiderman')
elif puede_volar is False and es_humano is True and tiene_mascara is False:
    print('El Heroe Es Hulk')
elif puede_volar is False and es_humano is False and tiene_mascara is True:
    print('El Heroe Es Black Bolt')
elif puede_volar is False and es_humano is False and tiene_mascara is False:
    print('El Heroe Es Thanos')