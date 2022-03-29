color=input('Digite que su color favorito: ')

match color:
    case 'Rojo':
        print('🔴')
    case 'Verde':
        print('🟢')
    case 'Azul':
        print('🔵')
    case _:
        print('Error')