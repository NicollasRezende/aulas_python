"""Geração automática de CPF"""

import random
import re

def calcula_digito(cpf):
  soma = 0
  contador = len(cpf) + 1
  
  for digito in cpf:
    soma += int(digito) * contador
    contador -= 1
  
  resto = 11 - (soma % 11)
  digito = 0 if resto > 9 else resto
  
  return digito

def gera_cpf():
  cpf = ''.join([str(random.randint(0,9)) for i in range(9)])
  
  digito1 = calcula_digito(cpf)
  digito2 = calcula_digito(cpf + str(digito1))
  
  novo_cpf = cpf + str(digito1) + str(digito2)
  return novo_cpf

for i in range(10):
  novo_cpf = gera_cpf()
  print(novo_cpf)

  #ja validados


