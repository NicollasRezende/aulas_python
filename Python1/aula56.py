# valor = input('usuario: ')
# condicao = valor == "10"
# variavel = print('valor' if condicao else 'nao valor')

cpf = input('CPF: ')
digitos_cpf = len(cpf)
cpf_2 = cpf if digitos_cpf == 11 else 'CPF invalido'

print(cpf_2)