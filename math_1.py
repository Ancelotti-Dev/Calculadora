#Dado um numero não negativo meu_numero
#Retorne a raiz quadrada de meu_numero arrendondada para o numero inteiro


import math

meu_numero = int(input("Digite o numero que deseja saber a Raiz: "))


resultado = math.sqrt(meu_numero)
if resultado % 1 == 0:
    resultado = int(resultado)

print(resultado)
