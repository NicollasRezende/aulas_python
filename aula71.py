#e possicel criar indices dentro do dict durante o codigo



lista = {}



lista['nome'] = 'Nicollas'
lista['sobrenome'] = 'Rezende'
#adiciona indices

print(lista['nome'])




if lista.get('sobrenome') is None: #.get serve como uma especie de try
    print('Nao existe')
else:
    print(lista['sobrenome'])


del lista['sobrenome'] #deleta o indice sobrenome

