#frase#


frase = 'Phython e uma linguagem de programaçao multiparadigma, phython foi criado por' \
'Guido van Rossum'

i = 0
qtd_aparecu_mais = 0
letra_apareceu_mais = " "

while i < len(frase):
    letr_atual = frase[i]
    letra_apareceu = frase.count(letr_atual)
    if letr_atual == " ":
        i += 1
        continue

    if qtd_aparecu_mais < letra_apareceu:
        qtd_aparecu_mais = letra_apareceu
        letra_apareceu_mais = letr_atual
        
    
    i += 1
print(f'letra que apareceu mais vezes foi:{letra_apareceu_mais}, e a letra se repetiu:{qtd_aparecu_mais} vezes')