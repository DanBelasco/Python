print(f'\n\n\n{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa separador de nomes ":=^90}\n\n')


nome = str(input('Digite o seu nome completo \n >>> ')).strip().split()


print(f'\nPrimeiro nome: {nome[0]}')
tamanho = len(nome) -1
print(f'\nUltimo nome: {nome[tamanho]}')

print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')

