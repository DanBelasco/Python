
k1 = input('\nDigite Algo  ')

print(f' O tipo primitivo digitado é {type(k1)}')

print(f' É numerico? {k1.isnumeric()}')
print(f' É decimal? {k1.isdecimal()}')
print(f' É alfabetico? {k1.isalpha()}')
print(f' É tudo minusculo? {k1.islower()}')
print(f' É identificador? {k1.isidentifier()}\n')