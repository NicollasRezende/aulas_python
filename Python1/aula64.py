'''
return
'''



def soma(x, y):
    if x > 10: #posso fazer uma condiçao para que o return ser executado
        return x + y#força a funçao a retornar este valor pois se nao houvesse isso ela retornaria none
        #nada pode executar depois do return
    else:
        print('nada')

soma1 = soma(11,4)
soma2 = soma(11,3)

print(soma1 + soma2)


