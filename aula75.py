while True:

    perguntas = {
        'Pergunta1': 'Quanto e 1+1: ',
        
        'opçoes':['(a)2., (b)22, (c)40'],

        'Resposta1': 'a',
        
        'Pergunta2': 'Quanto e 2*2: ',
        
        'opçoes2':['(a)20., (b)22, (c)4'],

        'Resposta2': 'c',
        
        'Pergunta3': 'Quanto e 5*5: ',

        'opçoes3':['(a)55., (b)25, (c)60'],
        
        'Resposta3': 'b',
    }



    #Perguntas

    
    print('ESCOLHA AS OPÇOES A B OU C')
    print(perguntas['Pergunta1'])
    print(perguntas['opçoes'])
    resposta_1 = input('Resposta: ')

    print()

    print(perguntas['Pergunta2'])
    print(perguntas['opçoes2'])
    resposta_2 = input('Resposta: ')

    print()

    print(perguntas['Pergunta3'])
    print(perguntas['opçoes3'])
    resposta_3 = input('Resposta: ')


    #Verificaçao

    errou1 = resposta_1 != perguntas['Resposta1']


    errou2 = resposta_2 != perguntas['Resposta2']


    errou3 = resposta_3 != perguntas['Resposta3']


    acertou1 = resposta_1 == perguntas['Resposta1']


    acertou2 = resposta_2 == perguntas['Resposta2']


    acertou3 = resposta_3 == perguntas['Resposta3']


    acertos = 0


    erros = 0

    #--confere erro e acerto


    if acertou1:
        acertos += 1
    else:
        erros +=1


    #--confere erro e acerto


    if acertou2:
        acertos += 1
    else:
        erros +=1


    #--confere erro e acerto


    if acertou3:
        acertos += 1
    else:
        erros +=1

    #resultados


    print()

    print(f'suas respostas foram: {resposta_1}, {resposta_2}, {resposta_3}')

    print()

    print(f'as respostas corretas eram: #1{perguntas["Resposta1"]}, #2{perguntas["Resposta2"]}, #3{perguntas["Resposta3"]}')

    print()

    print(f'Erros:{erros}, Acertos:{acertos}')

    print()

    print('Deseja jogar Novamente?')
    sair_naosair = input('[S]im, [N]ão: ')

    if sair_naosair == 'n':
        break
    elif sair_naosair == 's': 
        continue
