texto = "Python"

i = 0
tamanho_da_string = len(texto)


while i < tamanho_da_string:
    print(texto[i])
    
    
    i += 1  
 

senha =  "1234"


while True:

   
    senha_digitada = input('Digite a senha: ')

    if senha_digitada != senha:
        print('Voce errou, tente novamente: ')
        continue
    if senha_digitada == senha:
        print('Bem, Vindo.')
        break 



texto = 'Python'

for letra in texto:
    print(letra)