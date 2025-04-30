
# Exemplo de uso do yield em Python
# O yield é uma palavra-chave em Python que transforma uma função em um gerador.
# Isso significa que a função pode ser pausada e retomada, permitindo que ela retorne valores um de cada vez, em vez de retornar todos de uma vez.

def teste():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
# Se o gerador não for chamado com next, ele não vai executar o código
    yield 6


contador = teste()

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
# Se o gerador não for chamado com next, ele não vai executar o código
# E aparece <generator object teste at 0x0000021E637B5E80>
print(contador)
print(contador)
print(contador)
print(contador)
print(contador)
#Aqui eu chamei o gerador novamente com o 6
print(next(contador))
