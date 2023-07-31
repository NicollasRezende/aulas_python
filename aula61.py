'''
argumentos nomeados sao usados para mudar a ordem 
caso voce passe um argumento nomeado os seguintes tambem devem ser nomeados
  '''




def f(x,y,z):

    print(x, y, z)



f(1,2,3) #argumentos nao nomeados

f(z=3, x=1, y=2) #argumentos nomeados

f(1, y=2, z=3) #depois do argumento nomeado voce tambem deve nomear os outros argumentos