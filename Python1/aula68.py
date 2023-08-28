

def saudacao(saudacao):
    def saudar(nome):
        return (f'{saudacao},{nome}!')
    return saudar


s1 = saudacao('eae')
s2 = saudacao('salve')

print(s1('Man'))
print(s2('Man'))


for nome in ['Maria', 'Joao', 'Man']:
    print(s1(nome))