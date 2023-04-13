def fute(nome = '', gols =''):

    print('\n\n')
    
    nome = str(input('Nome do jogador: >>> ')).strip()

    if nome == '':
        nome = '<desconhecido>'
    
        
    gols = str(input('Número de gols: >>> ')).strip()

    if gols == '':
        gols = 0
    if gols == str:
        gols = 0

    print(f'\nO jogador {nome} fez {gols} gol(s) no campeonato')


#################################

fute()

print('\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
