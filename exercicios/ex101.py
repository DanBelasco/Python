#voto 16 até 17 opcional
# < 16 ñ pode
# > acima de 18 obrigatório
def voto():
    from datetime import datetime
    global atual
    atual = datetime.today().year

    global a
    a = int(input('Que ano você nasceu?  >>> '))

    if (atual - a) >= 18 and (atual - a) <= 69:
        return f'Com {atual - a} anos é obrigatótio a votar'
    
    elif (atual - a) == 16 or (atual - a) == 17:
        return f'Aos {atual - a} anos é opcional votar'  

    elif (atual - a) < 16:
        return f'Com {atual - a} anos você ainda não pode votar'
    
    elif (atual - a) >= 70:
        return f'depois dos {atual - a} anos o voto é opcional'

    
#-------------------------------------------
print('\n\n')
print('=-'*30)

print(voto())


print('\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
