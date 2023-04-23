
linhas = 1
mostrador = 10
c = 1
num = int(input('\n\nDigite o primeiro termo  \n\n  >>>> '))
razao = int(input('Digite o valor da Razão \n\n  >>>> '))
while mostrador != 0:
    while c <= mostrador:
        print(f'[{linhas}] {num} ')
        num = num + razao
        c = c + 1
        linhas = linhas +1
    
    mostrador = int(input('\nQuantas linhas dejesa mostrar a mais? \n \033[33mDigite "0" para sair\033[m \n\n >>>'))
    c = 1
   
print(f'\n\nSua ultima progreção foi de {num - razao} e ao todo foram visualizadas {linhas -1} linhas \n\n\n')
