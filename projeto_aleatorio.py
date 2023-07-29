#criar usuario senha/ pedir usuario senha/ verificar dados/ dar opçoes de interface.


#variaveis:

#criaçao dos dados do user    
criar_login = input('Crie seu login: ')#cria o login e armazena os dados
criar_senha = input('Crie sua senha: ')#cria o login e armazena os dados
lista = [] #armazena os dados
#codigo

while True:#enquanto true, loop infinito

    #pede os dados do usuario
    login = input('Digite seu login: ') #pede os dados
    senha = input('Digite sua senha: ')
    

    #variavei de conferencia de dados do usuario
    errou_senha = senha != criar_senha
    errou_login = login != criar_login
    errou_senha_e_login = errou_senha and errou_login
    acertou_dados = senha == criar_senha and login == criar_login
    
    #acertou os dados
    if acertou_dados:
        print('BEM VINDO!')
        print('O que deseja realizar:')
        opcoes = input('[a]Sair, [b]Adicionar um recado, [c]Apagar um recado, [d]Ver lista de recados.')#recebe os dados do usuario
    if opcoes == 'a': #opçao para parar o programa
        print('Ate mais.')
        break #para o programa
    if opcoes == 'b': #adiciona dados a lista onde ficam armazendos os dados que o user passar
        print('escreva o recado que deseja adicionar:')
        recado = input('')
        lista.append(recado)#funçao que adiciona o dado passado por meio do input recado
    if opcoes == 'c':#apagar algum dos dados inseridos dentro da lista
        print('Qual recado deseja apagar')

        for elementos, lista in enumerate(lista):
            print(elementos, lista)
        
        remover = input('Selecione o indice que deseja remover: ')
        del lista[remover]#apaga elementos da lista
    if opcoes == 'd':#mostra ao usuario a lista com os dados inseridos
        if lista == '':#se a lista estiver vazia ele nao mostra nada
            print('nao a nada na lista')
        else:#se houver dados str dentro da lista ele mostra a lista numerada
            print('Aqui esta sua lista:')
            for elementos, lista in enumerate(lista):
                print(elementos, lista)                
        
    #errou algum ou os dois dados de login
    #possiveis erros de login
    if errou_senha_e_login:
        print('Voce errou senha e login, tente novamente.')
    elif errou_senha:
        print('voce errou a sua senha, tente novamente.')
        continue
    elif errou_login:
        print('voce errou seu login, tente novamente.')
        continue


                                                            #codigo alternativo


                                                            #tentei fazer um codigo altenativo compactando ele o maximo possivel




# criação de classe Usuario para armazenar os dados do usuário
class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

# criação de classe Recados para armazenar a lista de recados        
class Recados:
    def __init__(self):
        self.recados = []
        
    def adicionar(self, recado):
        self.recados.append(recado)
        
    def remover(self, indice):
        del self.recados[indice]
        
    def listar(self):
        for i, recado in enumerate(self.recados):
            print(i, recado)
            
# código principal
usuario = Usuario(input('Crie seu login: '), input('Crie sua senha: ') )
recados = Recados()

while True:
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    
    if login == usuario.login and senha == usuario.senha:
        print('BEM VINDO!')
        
        opcao = input('O que deseja realizar? [a]Sair [b]Adicionar recado [c]Remover recado [d]Listar recados')
        
        if opcao == 'a':
            print('Até mais!')
            break
        
        elif opcao == 'b':
            recados.adicionar(input('Digite o recado: '))
            
        elif opcao == 'c':
            recados.listar()
            recados.remover(int(input('Qual índice deseja remover? ')))
            
        elif opcao == 'd':
            recados.listar()
            
    else:
        print('Login ou senha incorretos. Tente novamente.')