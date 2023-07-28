'''
faça uma lista de compras 
onde o usuario pode inserir apagar e listar os valores
nao permita que o programa quebr com erros de indices inexistentes na lista

'''


lista_de_compras = []
lista_de_compras_enumerada = enumerate(lista_de_compras)

while True:
    usuario = input('Deseja [I]inserir, [C]lear ou [L]istar: ')
    
    if usuario == 'i':
        lista_de_compras.append(input('O que deseja inserir: '))
        print(lista_de_compras)
        continue

    elif usuario == 'c':
        lista_de_compras.clear
        print(lista_de_compras)
        continue

    elif usuario == 'l':
        for elemento in lista_de_compras_enumerada:
            print(elemento)
        continue

    else:
        print('voce nao digitou nada')
        continue


