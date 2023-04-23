from time import sleep
from modulosss.uteis.encerra import cabô

listaDePessoas = [] 

def head(msg):
    print(f'-'*60)
    print(f'{msg:^60}')
    print(f'-'*60)

def menu():
    print('1 -- \033[34mVer pessoas cadastradas\033[m')
    print('2 -- \033[34mCadastrar nova pessoa\033[m')
    print('3 -- \033[34mSair do sistema\033[m')
    print('-'*60)

def erro():
    print('\n\033[41mValor incorreto!\033[m\n')

def TxT():

     
    listaDePessoas2 = ' '

    listaDePessoas2 = ''.join(listaDePessoas)


    arqTexto = open('zLista_Ex115.txt', 'a') # 'a' Serve para Subescrever mesmo ja tendo algo escrito no arquivo TXT

    arqTexto.writelines(f'{listaDePessoas2}')

    arqTexto.close()


def cadastro():
  

    while True: 

        while True:
            try:
                nome = str(input('Nome: ')).strip().capitalize()
            except:
                erro()                                      #Recebendo nome
            else:
                listaDePessoas.append(f'{nome};')
                print('\033[32mNOME ADICIONADO NA LISTA\033[m')
                break

        while True:
            try:
                idade = int(input('Idade:'))
            except:
                erro()                                      #Recebendo Idade
            
            else:
                if idade > 150 or idade < 0:
                    erro()
                else:
                    listaDePessoas.append(f'{str(idade)}\n')
                    print('\033[32mIDADE ADICIONADO NA LISTA\033[m')
                    break

        res = ''
        while res != 'SN':
            try:
                res = str(input('\nCadastrar outra pessoa?\n \033[33m[S/N]: >>>\033[m ')).strip().upper()
            
            except:
                erro()
            
            else:
                if res == 'S' or res == 'N':
                    break
                    

                if res not in 'NS':
                    erro()
        if res == 'N':
            break
    

def mostraLista():
    arqTexto = open('zLista_Ex115.txt','r')
    arqLista = arqTexto.readlines()
    
    for linha in arqLista:
        separador = linha.split(';')
        print(f'{separador[0]:.<30} {"idade:"}{separador[1]:>5}')

####################
#Programa Principal#
####################

print('\n\n')

while True:
    
    head('Menu Principal')
    menu()
    while True:
        try:
            escolha = int(input('\033[33mSua escolha: >>>\033[m '))
        
        except:
            erro()
            head('Menu Principal')
            menu()
        
        else: break
        
    if escolha >3 or escolha < 1:
        erro()


    if escolha == 3: ###  EXIT
        sleep(1)
        head('Obrigado e volte sempre!')
        sleep(1)
        cabô()
        break

    if escolha == 2: ### CADASTRO
        sleep(1)
        head('NOVO CADASTRO')
        sleep(1)
        listaDePessoas = []
        cadastro()
        TxT()
        
        sleep(2)

    if escolha == 1: ### Visualizar a lista de pessoas 
        sleep(1)
        print()
        head('PESSOAS CADASTRADAS')
        sleep(1)
        mostraLista()
        sleep(2)

