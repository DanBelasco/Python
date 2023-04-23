


termo = int(input('Digite o número do primeiro termo \n >>>'))

razao = int(input('Digite a Razão da P.A.'))

contador = 1
print(f'[1] {termo}')
for c in range(1,10,):
    termo = termo + razao
    contador = contador +1
    print(f'[{contador}] {termo}')