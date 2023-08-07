
#Soluçao 1

# numero = input('Digite: ')


# def duplica(numero):
#     return f'{numero * 2} Duplicado'
    
# def triplica(numero):
#         return f'{numero * 3} Triplicado'

# def quadriplica(numero):
#     return f'{numero * 4} quadriplicado'


# print(quadriplica(int(numero)))
# print(triplica(int(numero)))
# print(duplica(int(numero)))

#Soluçao 2

numero_ = int(input('Digite: '))

def criar_multiplicador(multiplicador):
    def numero(numero):
        return multiplicador * numero
    return numero







duplica = criar_multiplicador(2)
triplica = criar_multiplicador(3)
quadriplica = criar_multiplicador(4)

print(f'{quadriplica(numero_)} {numero_}X4')
print(f'{duplica(numero_)} {numero_}X2')
print(f'{triplica(numero_)} {numero_}X3')

