def errMsg(l):
    print(f'\n\033[41mERRO.\033[m " {l} " não é um valor monetário!\n')



def leiaDinheiro():
    flag = False

    while flag == False:
        
        n = str(input('\n\nDigite um valor R$:')).strip().replace(',','.')
        
    
        if n.isalpha() or n == '':
            errMsg(n)

        else:
             flag = True
             return float(n)
    
    print('\n\nCABO')


