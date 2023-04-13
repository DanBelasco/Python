

cont = 0
while True:
    n = int(input('\n\n Qual número você quer ver a Taboada ?  >>>'))
    if n < 0:
        break
    print(f'\n')
    print(f'\n{"-="*8}')
    while cont != 11:
        print(f' {n} x {cont} = {n*cont} ') 
        
    
        cont = cont +1
    print(f'{"-="*8}')
    cont = 0
    


