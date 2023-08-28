# def executa(funcao, *args):
#     return funcao(*args)



# duplica = executa(lambda n: lambda m: n * m, 2)

# print(duplica(9))

# definitivamente nunca faça isso ^^^^


def multiplicador(x):
    def numero(y):
        return x * y
    return numero


multiplicador_ = multiplicador(2)


print(multiplicador_(5))

#isso e legivel^^^^