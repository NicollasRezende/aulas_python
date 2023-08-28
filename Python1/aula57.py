"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
     012 345 678
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

import re
import sys
cpf = re.sub(r'[^0-9]', '', input('Digite Seu CPF: '))
#primeiro digito

repetiu = cpf == cpf[1] * len(cpf)

if repetiu:
    print('Invalido')
    sys.exit()

nove_digitos = cpf[:9]
contador1 = 10
resultado1 = 0
for digito_1 in nove_digitos:
    resultado1 += int(digito_1) * contador1
    contador1 -= 1

digito_1 = resultado1 * 10 % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


#segundo digito
dez_digitos = cpf[:10]
contador2 = 11
resultado2 = 0
for digito_2 in dez_digitos:
    resultado2 += int(digito_2) * contador2
    contador2 -= 1

digito_2 = resultado2 * 10 % 11
digito_2 = digito_2 if digito_1 <= 9 else 0


if str(digito_2) == cpf[10] and str(digito_1) == cpf[9]:
    print(f'{cpf}, Valido')
else: 
    print('Ivalido')


