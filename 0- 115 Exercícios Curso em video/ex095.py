listaDejogador = []
dadosJogador = {}

totalDeGols = 0
print("\n\n")
while True:
    gols = []                                                                                                           
    print('--'*35)
    dadosJogador["nome"] = str(input('Digite o nome do Jogador: >>>  ')).strip().capitalize()
    dadosJogador["partidas"] = int(input('Quantidade de partidas:  >>>  '))
    
    print('')
    
    for c in range (0,dadosJogador['partidas']):
        gols.append(int(input(f'Quantos gols o jogador {dadosJogador["nome"]} fez na {c+1} partida?  >>>  ')))

    dadosJogador["gols"] = gols

    total = sum(gols)
    dadosJogador["total"] = total
    
    listaDejogador.append(dadosJogador.copy())
    

    
    res = ' '
    while res not in 'SN':
        res = str(input('\033[33mDeseja continuar?\033[m  \n [\033[32mS\033[m/\033[31mN\033[m] >>> ')).strip().capitalize()[0]
    if res == 'N':
        break
   
#-----------------------------------------


print('\n\n\n')
print('=-'*35)
print(f'{"Cód "}', end='')#  Cabeçalho dos itens na lista
for l in dadosJogador.keys():
    print(f'|{l:<14}', end='')
print('')
print('--'*35)

for k, v in enumerate(listaDejogador):
    print(f'{k:>3} ' ,end='')  # itens contidos na tabela
    for m in v.values():
        print(f'{str(m):<15}' , end='')
    print('')
print('=-'*35)

print('')

while True:

    res = ' '
    res = str(input('\n\033[32mDigite os código do jogador que deseja saber os dados\033[m \n [999] P/ encerrar >>> ')).strip()
    if res == '999':
        break
    elif res == ' ':########################  filtro de entrada de valores
        res = '998'
    elif res == '':
        res = '998'
    elif int(res) < 0:
        res = '998'

    if int(res) >= (len(listaDejogador) ) :
        print("\n \033[41mNúmero inválido!\033[m\n Digite um valor contido na lista acima!")


    else:
        print('\n\n')
        print('=-'*35)
        print(f'            -- Levantamento de dados do jogador {listaDejogador[int(res)]["nome"]} --')
        print('=-'*35)

        for n, j in enumerate(listaDejogador[int(res)]['gols']):
            print(f'--== No jogo {n+1} fez {j} gols ==-')
        print('=-'*35)



print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
print('\n\n')