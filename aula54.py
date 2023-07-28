
lista_de_compras = []

import os

while True:
    #recebe os comandos
    
    print('selecione uma opçao')
    usuario = input('Deseja [i]inserir, [r]emover ou [l]istar: ')
    os.system('clear')
    #inserir valores
    if usuario == 'i':
        
        valor = input('O que deseja inserir: ')
        lista_de_compras.append(valor)
        os.system('clear')
        continue
    #listar valores
    elif usuario == 'l':
        
        for i, valor in enumerate(lista_de_compras):
            print(i, valor)
            continue
        if len(lista_de_compras) == 0:
            print('Nada para listar')
        os.system('clear')
    #remove os valores
    elif usuario == 'r':
        
        for i, valor in enumerate(lista_de_compras):
            print(i, valor)
        indice_str = input('O que deseja apagar: ')
        try:
            indice = int(indice_str)
            del lista_de_compras[indice]
            os.system('clear')
            continue
        except ValueError:
            print('Digite apenas numeros')
            os.system('clear')
            continue
        except IndexError:
            print('Esse indice nao existe')
            os.system('clear')
            continue
    #se nenhuma das opçoes escolhidas for digitada
    else:
        print('por favor escolha uma das opçoes [i], [l], [r]')


