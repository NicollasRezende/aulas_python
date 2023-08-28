import copy


d1 = {
    'c1': '1',
    'c2': '2',
    'd3': [0, 1, 3 ,4],
}


d2 = d1.copy() #copia o dicionario ou seja faz um novo dicionario permitindo alterações sem interferencia em d1
d3 = copy.deepcopy(d1) #copia mais profunda



d3['d3'][0] = 100
d2['c1'] = '100'


print(d1['c1'])#original 

print(d2['c1']) #copia rasa

print(d3['d3']) #copia profunda ou deep copy isso consegue copiar a lista e as sublistas fazendo com que voce consiga modificar



'''
adendo importante isso e uma copia rasa portanto nao entra em subniveis como lista dentro de lista 

'''
