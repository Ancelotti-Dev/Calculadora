#Lambda é usada para criar funções que podem ser passadas como argumentos para outras funções ou usadas como callbacks.
# Ela é útil quando você precisa de uma função simples e não quer definir uma função completa com def.


meu_array = [1, 2, 111,3, 4, 5, 6, 7, 10, 34, 24 ,12, 48, 15, 75]

# Aqui eu criei uma forma de fazer con o FOR e IN, desse jeito é mais fácil de entender mas é mais demorado e não eficiente para um gramde nÙmero de elementos
Meu_triplicados = []
for i in meu_array:
    Meu_triplicados.append(i*3)
    #Se o print ficar dentro do for, ele vai imprimir o resultado de cada iteração, e não o resultado final
    # print(Meu_triplicados)
    # print("*******************************************************")
print(Meu_triplicados)



# Com a função lambda, eu criei uma função que multiplica o valor por 3, e depois eu usei a função map para aplicar essa função a cada elemento do meu_array
# A função map aplica a função lambda a cada elemento do meu_array e retorna um iterador.
triplicados = map(lambda x: x * 3, meu_array)

# Aqui eu usei a função map para aplicar a função lambda a cada elemento do meu_array e depois eu converti o resultado para uma lista
triplicados = list(triplicados)

triplicados.sort()
print(triplicados)

print("*******************************************************")


quadriplicados = map(lambda x: x * 4,meu_array)

# Aqui eu usei a função map para aplicar a função lambda a cada elemento do meu_array e depois eu converti o resultado para uma lista
# Se o map não for convertido para uma lista, ele não vai imprimir no console, e vai aparecer <map object at 0x0000021E637B5E80>
quadriplicados = list(quadriplicados)

#Aqui print o resultado final da lambda
print(quadriplicados)

print("*******************************************************")


# Multpliquei por 134 para ver como sai o codigó perfeito e lambda é mais eficiente
multiplicado_134 = map(lambda x: x * 134,meu_array)

multiplicado_134 = list(multiplicado_134)

print(multiplicado_134)

# eu fiz a função sort para colacar elas em ordem crescente para descrecente
multiplicado_134.sort()
print(multiplicado_134)

# Aqui eu fiz a função sort para colar elas em ordem decrescente, e coloquei o reverse=True para inverter a ordem
multiplicado_134.sort(reverse=True)
print(multiplicado_134)