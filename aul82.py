lista = [
    'a', 1,2,3,'c','d',4
]


for item in lista:
    if isinstance(item, int):
        print(item*2)
    else:
        print(item, 'Nao e um numero')