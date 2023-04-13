print(f'\n\n\n{"":=^90}')
print(f'{" Icinializando ":^90}')
print(f'{"":=^90}\n')
print(f'\n{" Programa para escolher quem vai apagar a lousa ":=^90}\n\n')


from random import choice

n1 = input('Nome do primeiro aluno >>>')
n2 = input('Nome do segundo aluno >>>')
n3 = input('Nome do terceiro aluno >>>')
n4 = input('Nome do quarto aluno >>>')

lista = [n1,n2,n3,n4]

dado = choice(lista)
print(f'\nO aluno escolhido para apagar a lousa foi:    >>>{dado}<<<  ')

print(f'\n\n{"":=^90}')
print(f'{" Programa encerrado ":^90}')
print(f'{"":=^90}\n\n\n')