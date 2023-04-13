n1=4
n2=3
s=n1/n2
print(s)
print(f'{s:.3f} ')# Metodo utilizado para formatar o print. nesse caso para exibir somente 
# 3 casas decimais da dizima periodica


#é possivel alinhar o print também
print(f'{" Palavra Qualquer ":30} e outra coisa') #o ":30" diz para imprimir no console o restante
# da string depois de 30 caracteres em vazio

print(f'{" Palavra Qualquer ":=^30}') #foram digitados 30 "=" e alinhados com metade para
#cada lado e a string foi mantida centralizada pelo caractere "^"

print(f'{" Palavra Qualquer ":=>30}') # ja com ">" o alinhamento vai para direita. 
# o mesmo pode ser feito para a esquerda
print(f'{" Palavra Qualquer ":=<30}')

print(f'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',end="") # Adicionando [,end=""] ao fiinal da
# String é possivel juntar com o string do proximo print
print(f'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')

