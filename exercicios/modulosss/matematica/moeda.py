from modulosss.uteis.moeda_brasil import real

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

def aumento(a,b, formatar = False):
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
