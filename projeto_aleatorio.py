#criar usuario senha/ pedir usuario senha/ verificar dados/ dar opçoes de interface.


#variaveis:

#criaçao dos dados do user    
criar_login = input('Crie seu login: ')
criar_senha = input('Crie sua senha: ')
lista = []
#codigo

while True:

    #pede os dados do usuario
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    
    errou_senha = senha != criar_senha
    errou_login = login != criar_login
    errou_senha_e_login = errou_senha and errou_login
    acertou_dados = senha == criar_senha and login == criar_login
    
    #acertou os dados
    if acertou_dados:
        print('BEM VINDO!')
        print('O que deseja realizar:')
        opcoes = input('[a]Sair, [b]Adicionar um recado, [c]Apagar um recado, [d]Ver lista de recados.')
    if opcoes == 'a':
        print('Ate mais.')
        break
    if opcoes == 'b':
        print('escreva o recado que deseja adicionar:')
        recado = input('')
        lista.append(recado)
    if opcoes == 'c':
        print('Qual recado deseja apagar')

        for elementos, lista in enumerate(lista):
            print(elementos, lista)
        
        remover = input('Selecione o indice que deseja remover: ')
        del lista[remover]
    if opcoes == 'd':
        print('Aqui esta sua lista:')
        for elementos, lista in enumerate(lista):
            print(elementos, lista)                
    
    #errou algum ou os dois dados de login
    if errou_senha_e_login:
        print('Voce errou senha e login, tente novamente.')
    elif errou_senha:
        print('voce errou a sua senha, tente novamente.')
        continue
    elif errou_login:
        print('voce errou seu login, tente novamente.')
        continue


                                                            #codigo alternativo




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