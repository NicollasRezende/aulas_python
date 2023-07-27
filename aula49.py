"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

# lista = [10, 20, 30, 40] #lista criada
# lista[2] = 300 #mudar o valor do indice
# del lista[2] #aqui o indice 2 vira 40
# lista.append(input('digita algo: '))#inserir valor a lista
# print(lista) #mostra o valor do indice marcado
# lista.pop()#remover valores adicionados ou ja presentes.
# print(lista)


# lista2 = ['nome', 'senha', 0]

# lista2[0] = input('digite seu nome: ')
# lista2[1] = input('digite sua senha: ')
# lista2[2] = input('digite um numero: ')
# lista2.append(input('Digite uma coisa qualquer: '))

# print(lista)

# print(f'seu nome e "{lista2[0]}", sua senha e "{lista2[1]}", o numero digitado foi "{lista2[2]}", e voce digitou "{lista2[3]}"') #o usuario pode mudar o valor do indice.



# lista3 = ['a', 'b', 'c',]

# lista3.insert(1, 'ola')#isso adiciona itens a lista podendo mover itens de lugar 

# print(lista3)


# lista4 = ["a"]

# lista4.clear()#limpa a lista toda

# print(lista4)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b #uniu as listas
lista_b = lista_a.extend(lista_b) #tambem uniu as listas

print(lista_a)
print(lista_b)#None pq executa uma açao
print(lista_c)
print(lista_b)#None pq executa uma açao


