#Define uma classe chamada Animal com os atributos nome e idade.(Vai ser a Superclasse)
class Animal:
    def __init__(self,nome,idade): # Método construtor (__init__) que inicializa um objeto Animal
        self.nome = nome # Atribui o valor do parâmetro ao atributo 'nome' do objeto
        self.idade = idade # Atribui o valor do parâmetro ao atributo 'idade' do objeto

    def mostrar_animal(self):
        print(f"Nome do animal: {self.nome} | Idade do animal: {self.idade}")

    def emitir_som(Animal):
        print("O animal emitiu um som generico")

#class Cachrro herda de Animal e implementa o método emitir_som
class cachorro(Animal):
    def emitir_som(self):
        print("o cachorro latiu!")


class gato(Animal): # Definição da classe Gato, que herda da classe Animal
    def emitir_som(self):  # Sobrescrita do método emitir_som para um comportamento específico de Gato
        print("O gato miou!") # Retorna o som característico do gato


cachorro = cachorro("theo", 3)
gato = gato("nala", 6)

cachorro.emitir_som()
cachorro.mostrar_animal()
gato.emitir_som()
gato.mostrar_animal()

