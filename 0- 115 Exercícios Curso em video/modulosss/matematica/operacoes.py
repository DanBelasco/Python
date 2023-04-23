'''

O modulo "Uteis" foi criado por minha autoria e está presenta na mesma pasta que o arquivo "modulos"

sendo assim, necessário para o funcionamento, tanto código atual quanto codigo de "modulos", juntos no mesmo projeto.

O modulo "uteis" prove para o codigo "modulos" 4 funções diferentes. sendo elas:

*Fat - Calcula o fatorial de uma numero
*dobro - Calcula o dobro de um numero
*triplo - Calcula o triplo de um numero
*ipo -  calcula a hipotenusa de um numero

OBS: É possivel importar todo o pacote de modulos utilizando asterisco (*) depois de > from uteis import <. Ao invés de
importar somente uma parte do pacote. Ou importar tudo e ter que utilizar ".uteis" antes de qualquer função do pacote.


'''



def fat(n):
    f = 1
    for c in range(1, n + 1):
        f = f * c 
    return f


def dobro(n):
    return n *2


def triplo(n):
    return n * 3


def ipo(a,b):
    f = (a**2) + (b**2)
    c = f** (1/2)
    return c