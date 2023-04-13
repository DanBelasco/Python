from modulosss.uteis.moeda_brasil import real
from modulosss.uteis.encerra import cabô

def dobro(n,formatar = False):
    '''
    Retorna o dobro do valor de 'n'
    
    '''
    n = n*2
    if formatar == True:
        n = f'R${n:.2f}'.replace('.',',')
        return n 
    return n

def metade(n, formatar = False):
    '''
    Retorna a Metade do valor de 'n' 
    '''
    n = n / 2
    if formatar == True:
        n = real(n)
        return n
    return n

def aumento(a,b=10, formatar = False):
    '''
    (a) = valor
    
    (b) = porcentagem
    
    '''
    t =  a + (a * (b/100))
    if formatar == True:
        t = real(t)
        return (t)
    return t

def diminui(c,d,formatar = False):
    '''
    (c) = valor
    
    (d) = porcentagem
    
    '''
    r = c - (c * (d/100))
    if formatar == True:
        r = real(r)
        return r
    return r



def resumo(n,aumen=10,reduc=5):
    tamamho = 50
    print('')
    print(f'='*tamamho)
    print(f'{"RESUMO DO VALOR":^{tamamho}}')
    print(f'='*tamamho)
    print('')

    print(f'{"VALOR INFORMADO:":.<30}{(real(n)):.>20}')
    print(f'{"Dobro do preço é:":.<30}{dobro(n, formatar=True):.>20}')
    print(f'{"Metado do preço é:":.<30}{metade(n, formatar=True):.>20}')
    print(f'{"Aumento de ":.<}{aumen:.<}{"% no preço é:":.<}{aumento(n,aumen,formatar=True):.>24}')
    print(f'{"Redução de ":.<}{reduc:.<}{"% no preço é:":.<}{diminui(n,reduc,formatar=True):.>24}')
    print(f'='*tamamho)
    
    cabô()