#calculadora com while
while True:
    
    
        #--------------------------#
    


    print('Escolha os numeros')
    numero_1 = input('Digite o primeiro numero: ')
    operador = input('Digite o operador [+], [-], [/], [*]: ')
    numero_2 = input('Digite o segundo numero: ')
    
    print(f'o RESULTADO de {numero_1} {operador} {numero_2} e:')


        #--------------------------#
    
        #variaveis:

    numeros_validos = None
    operadores_validos = '+-/*'
    numero_1int = 0
    numero_2int = 0


        #--------------------------#


    try:
        
        numero_1int = int(numero_1)
        numero_2int = int(numero_2)   
        numeros_validos = True 


    
        if operador == '+':
            print(numero_1int + numero_2int)
        
        elif operador == '-':    
            print(numero_1int - numero_2int)
        
        elif operador == '/':
            print(numero_1int / numero_2int)
        
        elif operador == '*':
            print(numero_1int * numero_2int)
        
        #--------------------------#    


    except:
        numeros_validos = None

        if numeros_validos is None:
            print("Erro")
            continue

        if operador not in operadores_validos:
            print("Erro")
            continue
       
        if len(operador) > 1:
            print("Erro")
            continue
    
    

    
        #--------------------------# 
    sair = input('Deseja reiniciar a calculadora? [S]im: ').lower

    if sair == 'sair':
        break