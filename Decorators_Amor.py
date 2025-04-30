
#Exeplo de Decorator em Python
# Decorators são uma maneira de modificar o comportamento de funções ou métodos em Python.
# Eles permitem adicionar funcionalidades a uma função existente sem modificar seu código original.
# Decorators são frequentemente usados para adicionar funcionalidades como autenticação, registro, controle de acesso, etc.


def amor(func):
    def wrapper():
        print("gostei dessa pessoa!")
#ESSA FUNÇÃO FUNC È A FUNÇÂO DEU VOCÊ QUE QUER CHAMAR, NO CASO A FUNÇÃO CONHECENDO
        func()
        print("Vamos se casar?")
        if True:
            print("sim, Eu aceito!")
#Retorna a função wrapper, que é a função que vai ser chamada quando o decorator for aplicado
    return wrapper



def Pedido():
    print("Somos o casal Perfeito, Vamos ser Felizes para Sempre!")



def Brigas():
    print("briguinhas de casal são normais!")
    print("Brigas são normais")
    print("Supera as brigas, e vamos ser felizes juntos!")
    print("Ele é só um amigo meu!, não é nada demais!")
    print("Muitas brigas")
    print("Desespeito com outro")
    print("Brigas")
    print("Distanciamento, não se amam mais!")


def Divorcio():
    print("Toda historia de Amor tem um fim!")


# Chamando a Funçaõ Decorator com a função Wrapper com @
@amor
def Conhecendo():
    print("Oii, Eu te vi no intagram!")
    print("Nossa você é muito linda!")
    print("Vamos sair juntos?")
    print("Eu gostei muito de Você, Temos muitas coisas em comum!")
    print("3 ENCONTROS DEPOIS")
    print("eu amo muito voce!")


# Aqui Serve paara Ordenar a execução do código, e não deixar que o código seja executado antes de ser chamado

Conhecendo()
Pedido()
Brigas()
Divorcio()