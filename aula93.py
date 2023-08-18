import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumentar os preços dos produtos em 10%
for produto in produtos:
    produto['preco'] *= 1.1

# Criar uma cópia profunda dos produtos
novos_produtos = copy.deepcopy(produtos)

# Ordenar os produtos por nome decrescente
produtos_ordenados_por_nome = sorted(produtos, key=lambda x: x['nome'], reverse=True)

# Criar uma cópia profunda dos produtos ordenados por nome
produtos_ordenados_por_nome = copy.deepcopy(produtos_ordenados_por_nome)

# Ordenar os produtos por preço crescente
produtos_ordenados_por_preco = sorted(produtos, key=lambda x: x['preco'])

# Criar uma cópia profunda dos produtos ordenados por preço
produtos_ordenados_por_preco = copy.deepcopy(produtos_ordenados_por_preco)

# Função para exibir os produtos de forma legível
def exibir_produtos(produtos_lista):
    for produto in produtos_lista:
        print(f"Produto: {produto['nome']}, Preço: R$ {produto['preco']:.2f}")

# Imprimir os resultados
print("Produtos originais com preços aumentados:")
exibir_produtos(produtos)
print("\nCópia profunda dos produtos originais:")
exibir_produtos(novos_produtos)
print("\nProdutos ordenados por nome decrescente:")
exibir_produtos(produtos_ordenados_por_nome)
print("\nProdutos ordenados por preço crescente:")
exibir_produtos(produtos_ordenados_por_preco)