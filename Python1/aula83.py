
string = 'a'
dicionario = {'a'}
lista = ["a"]
tupla = ('a')


def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE', falsy('TESTE'))
print(f'string',falsy(string))
print(f'dicionario',falsy(dicionario))
print(f'lista',falsy(lista))
print(f'tupla',falsy(tupla))
