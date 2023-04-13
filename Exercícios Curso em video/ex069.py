
quantosComMaisDe18 = 0
totalDeHomens = 0
mulheresAbaixoDe20 = 0 
loira = 0
morena = 0 
ruivas = 0

print('='*40)
print(f'{"      Cadastramendo  de pessoas"}')
print('='*40)

while True:
    print(f'\n\n{"="*40}')
    print('         Cadastre uma pessoa')
    print(f'{"="*40}')
    idade = int(input('\n\nIdade? :'))
    sexo = '  '
    while sexo not in 'MF' :
        sexo =str(input('Sexo [M/F] ? : ')).strip().upper()[0]
    if sexo == 'F':
        cabelo = ' '
        while cabelo not in 'LMR':
                  cabelo = str(input('Qual a cor o seu cabelo?? [L/M/R]')).strip().upper()[0]
    
    if idade >18:
        quantosComMaisDe18 = quantosComMaisDe18 + 1
    
    if sexo == 'M':
        totalDeHomens =totalDeHomens + 1

    if sexo == 'F' and idade < 20:
        mulheresAbaixoDe20 = mulheresAbaixoDe20 + 1

    if sexo == 'F' and cabelo == 'L':
        loira = loira +1
    if sexo == 'F' and cabelo == 'M':
        morena = morena + 1
    if sexo == 'F' and cabelo == 'R':
        ruivas = ruivas + 1 

    continuar = ' '
    while continuar not in 'S'and continuar not in 'N':
        continuar =str(input('\nDeseja continuar? [S/N] ')).strip().upper()[0]
    if continuar =='N': break
    
    
    
print(f'\n\n{"="*48}')
print('                 \033[32mRESULTADO\033[m')
print('='*48)
print(f'\nForam registrados {quantosComMaisDe18} pessoas com mais de 18 anos ')
print(f'\nAo todo {totalDeHomens} homens.')
print(f'\nE {mulheresAbaixoDe20} mulheres com menos de 20\n')
if ruivas > 0 or morena > 0 or loira > 0 :
    print(f'temos {loira} loiras, {morena} morenas e {ruivas} ruivas nesse grupo\n')
    