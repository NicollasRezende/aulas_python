

def soma(x, y):
        print(x + y)
    
def multi(x,y):
        print(x*y)

def sub(x,y):
        print(x-y)

def div(x,y):
        print(x/y)



numero1 = input('Digite o Primeiro numero: ')

numero2 = input('Digite o Segundo numero: ')

opcoes = input('DIgite (+), (-), (*), ou (/): ')


if opcoes == '+':
    soma(int(numero1), int(numero2))


if opcoes == '-':
    sub(int(numero1), int(numero2))


if opcoes == '*':
    multi(int(numero1), int(numero2))


if opcoes == '/':
    div(int(numero1), int(numero2))

