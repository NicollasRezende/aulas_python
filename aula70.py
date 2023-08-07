
# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# altura = float(input('Digite sua altura: '))
# peso = float(input('Digite seu peso: '))

pessoa =  {

    'nome': 'nicollas',
    'idade': 18,
    'altura': 1.69,
    'peso': 69,
    'Endereço': [{'rua': 'tal tal', 'numero': 15},]



}

print(pessoa)

print()


for chave in pessoa:
    print(chave, pessoa[chave])

print()
carro = dict(pessoa= 'carro',)


print(carro)