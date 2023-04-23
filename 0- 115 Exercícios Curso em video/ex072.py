

numi =('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete' , 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = 0

while True:
    n = int(input('Digite o número entre 0 e 20 >>>>'))
    if n > -1 and n < 21:
        print(f'\n\nVoce digitou o numero \033[32m{numi[n]}\033[m\n\n')
    else:
        print('\n\ntente novamente.\n')

