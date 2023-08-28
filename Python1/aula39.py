""" 

iterando strings com while


 """

#       n i c o l l a s
#       0 1 2 3 4 5 6 7
#       n   i   c   o   l   l    a   s
#      -1, -2, -3, -4, -5, -6 , -7, -8



nome = 'nicollas'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)