def inicia():
    print('Inicia') #define uma variavel e quando ela for executada ou "chamada" ela executa o codigo dentro dela
    print('Inicia')
                    #usado para funçoes repetitivas


def inicia_2(a, b, c,):
    #e possivel definir parametros dentro da funçao criada
    #os parametros sao como variaveis
    print(a, b, c)



inicia_2(1, 2, 3)#defina o valor dos parametros aqui
inicia_2(4, 5, 6)#posso mudar os parametros quando quiser



def saudacao(nome='sem nome'):#posso definir um valor aqui tambem nesse caso se nada for atribuido quando ela for chamada isso e colocado no lugar
    print(f'ola {nome}')

saudacao('Carlos')
saudacao('jose')
saudacao()




#por padrao funçoes retornam none