
def leiaInt():
    while True:
        
        try:
            n = int(input('\n\nDigite um numero: '))

        except (ValueError,TypeError) :
            print(f'\n \033[31mEntrada de dados invalidos!\033[m  ') 
        
        except KeyboardInterrupt:
            print('\nComando Inválido')

        except Exception as cagada:
            print(f'\n Entrada de dados invalidos.\033[31mCagada\033[m ')
        
        else:
             print(f'\n\n \033[33mO numero digitado foi {n}\033[m')
             return n
        
            
            

def leiaFloat():
    while True:
        try: 
            n = float(input('\n\nDigite um numero do tipo Float: '))

        except (ValueError,TypeError):
            print(f'\n\n\033[31mEntrada de dados inválida!\033[m')
        except KeyboardInterrupt:
            print(f'\n\n\033[31mEntrada de dados inválida!\033[m')

        except Exception as cagada:
            print(f'\n\n\Entrada de dados inválida! \033[31mcagada\033[m')

        else:
            print(f'\n\n \033[33mO numero digitado foi {n}\033[m')
            return n
       
#######################

leiaInt()
leiaFloat()