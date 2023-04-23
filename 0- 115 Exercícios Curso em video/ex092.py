import datetime
cadastro = {}
ano_atual = datetime.date.today().year
print('\n\n')
cadastro["Nome"] = str(input('Nome : >>>  ')).strip().capitalize()
anonasc = int(input('Ano de nascimento: >>> '))
idade = (ano_atual - anonasc)                   
cadastro["Idade"] = idade
ctps = int(input('Nº CTPS: [0 para Ñ possui]>>> '))
if ctps == 0:
    cadastro["CTPS"] = "Não Possui "
    print('\n\n')
    print('=-'*25)
    print('Resumo do cadastro')
    print('=-'*25)

    for c ,d in cadastro.items():
        print(f' {c}: {d}')
else:
    anocontrata = int(input('Ano de contratação: >>>'))
    cadastro["Ano de Contratação"] = anocontrata
    aposentaEm = anocontrata + 35
    cadastro["Ano de aposentadoria prevista"] = aposentaEm
    cadastro["Idade de aposentadoria"] = str((ano_atual - anocontrata) + 35) + (" Anos") 
    cadastro["Salário"] = float(input('Faixa de salário: >>> ')) 
    print('\n\n')
    print('=-'*25)
    print('Resumo do cadastro')
    print('=-'*25)
    for q, w in cadastro.items():
        print(f'{q}: {w}')


print('\n\n')
print(f'\033[41m{" Programa encerrado ":^90}\033[m')
print('\n\n')
