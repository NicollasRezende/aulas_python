'''
introduçao ao desempacotamento + tuples(tuplas)
'''


nomes = ['Jorge', 'Carlos', 'Marcos'] #"pacote"


nome_1, nome_2, nome_3 = nomes #"desempacotando"

print(nome_3)
print(nome_2)
print(nome_1)


nome1, *resto = ['Maria', 'Jorge', 'Ricardo'] #"desempacotando" apenas um dos valores

print(nome1) #variavel "desempacotada"
print(resto)#variaveis que se manteram no "pacote"


# nome1, *_#isso indica que os restantes dos valores nao serao usados. = ['Maria', 'Jorge', 'Ricardo'] #"desempacotando" apenas um dos valores

