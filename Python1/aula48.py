"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321

string = 'ABCDE'  # 5 caracteres (len)


# print(bool([]))  # falsy
# print(lista, type(lista))

#acessar item por item de acordo com o indice.
        # 0    1     2      3         4
        #-1   -2    -3     -4        -5
lista = [123, True, 1.2, 'Nicollas', []]
lista[-3] = 'Maria'
print(lista[-3], type(lista[-3]))
print(lista)