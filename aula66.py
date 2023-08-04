
par_ou_impar = input("Digite um numero: ")

def numero_par_impar(par_ou_impar):

    e_par = int(par_ou_impar) % 2 == 0
    e_impar = int(par_ou_impar) % 2 != 0

    if e_par:
        print(f'seu numero e par, aqui esta a multiplicação dos numneros: {int(par_ou_impar) % 2}') 
    elif e_impar:
        print(f'seu numero e impar, aqui esta o resto da divisao por 2: {int(par_ou_impar) % 2}')
    
numero_par_impar(par_ou_impar)


multi1 = input('Digite o primeiro valor: ')
multi2 = input('Digite o segundo valor: ')

def multiplicacao(a,b):
    try:
        print(int(a) * int(b), ', Esse e o resultado da sua multiplicaçao')
    except(ValueError):
        print("voce digitou uma letra")


multiplicacao(multi1, multi2)