def cor(p=3,c=0):
    print(f'\033[{p}{c}m')

def clean():
    print(f'\033[m')

def titulo(msg, cor=0):
    print('\n')
    tamanho = len(msg)
    print(f'='*(tamanho + 4))
    print(f'  \033[32m{msg}\033[m')
    print(f'='*(tamanho + 4))

def ajuda(comando):
    help(f'{comando}')
###########################################

from time import sleep


titulo('Sistema de ajuda interativo')
sleep(1)

res = ''
while res != 'SAIR':
    print


    res = str(input('\n\n\033[34mDigite o comando que desja obter ajuda\n Ou\033[m \033[33mSAIR\033[m \033[34mpara encerrar.\033[m   \n   \033[44m>>>\033[m  '))
    if res.upper() == 'SAIR':
        break
    
    titulo(f'acessando o manual do "{res}" ')

    sleep(1)
    cor(4,2)
    ajuda(res)
    clean()


titulo('Encerrando')
sleep(2)

print('\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
