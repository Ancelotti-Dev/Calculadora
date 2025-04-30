# Polimorfismo é um conceito de programação orientada a objetos que permite que objetos de diferentes classes sejam tratados como objetos da mesma classe através de uma interface comum. O polimorfismo é frequentemente utilizado em herança, onde uma classe filha pode substituir métodos da classe pai, permitindo que o mesmo método tenha comportamentos diferentes dependendo do objeto que o chama.

class ModePokemon:
# Aqui eu criei o construtor da classe ModePokemon, e coloquei os atributos que eu quero que a classe tenha
    def __init__(self, name, type1, type2, hp, attack, height, weight):
        self.name = name
        self.attack = attack
        self.type1 = type1
        self.type2 = type2 
        self.hp = hp
        self.height = height
        self.weight = weight
# Aqui eu criei o SElf para Pegar os Atribtos que passei para a classe ModePokemon, e coloquei o nome de cada atributo
    def mostrar_pokemon(self):
        if self.type2 == "none":
            print(f" O nome do pokemon é {self.name} | O tipo 1 dele é {self.type1} |  "
                  f"Ele tem {self.hp} HP | O attack dele é {self.attack} | Altura dele {self.height} | O peso dele {self.weight}")
        else:
            print(f" O nome do pokemon é {self.name} | O tipo 1 dele é {self.type1} | o tipo 2 dele é {self.type2}| "
          f"Ele tem {self.hp} HP | O attack dele é {self.attack} | Altura dele {self.height} | O peso dele {self.weight}")
            

#Aqui seria o Pokemon que eu criei, e coloquei os atributos que eu quero que ele tenha, Em ordem do Construtor que eu criei
pikachu = ModePokemon("Pikachu", "Electric", "none", 120, 55, 0.4, 6.0)
charizard = ModePokemon("Charizard", "Fire", "Flying", 150, 80, 1.7, 90.5)


# Aqui eu chamei a função mostrar_pokemon, e coloquei o nome do pokemon que eu quero que ele mostre os atributos
pikachu.mostrar_pokemon()
charizard.mostrar_pokemon()

