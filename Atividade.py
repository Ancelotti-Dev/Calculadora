# Crie um programa para gerenciar uma biblioteca de livros. O programa deve exibir um menu com as opções: adicionar livro, listar livros, remover livro, atualizar quantidade de livros, registrar empréstimo, exibir histórico de empréstimos e sair.

# Os livros serão armazenados em um dicionário onde a chave será o título do livro e o valor será outro dicionário contendo duas informações: a quantidade de exemplares disponíveis e o nome do autor. 

#DICIONARIOS CRIADOS
biblioteca = {}
historico_emprestimos = []



#  Quando o usuário escolher a opção de adicionar um livro, o programa deverá pedir o título do livro, o nome do autor e a quantidade de exemplares. Esses dados devem ser armazenados no dicionário.
def adicionar_Livro(biblioteca):
    titulo = input("Digite o titulo do Livro: ").strip()
    autor = input(f"Digite o Autor do {titulo}: ").strip()
    if titulo in biblioteca:
        print("livro já está cadastrado")
    try:
        quantidade = int(input("Digite a quantidade de exemplares: "))
        if quantidade < 0:
            raise ValueError
    except ValueError:
        print("Quantidade inválida. Use um número inteiro positivo.")
    biblioteca[titulo] = {"Autor": autor, "Quantidade": quantidade}
    print(f" Livro: {titulo} - Autor: {autor} - Unidades: {quantidade} disponíveis")


# Na opção de listar livros, o programa deve exibir todos os livros cadastrados no formato: título do livro - autor - quantidade disponível. Os livros devem ser ordenados alfabeticamente por título.
def listar_livros(biblioteca): 
    for titulo in sorted(biblioteca.keys()):
        autor = biblioteca[titulo]["Autor"]
        quantidade = biblioteca[titulo]["Quantidade"]
        print("===================================")
        print(f" Livro: {titulo} - Autor: {autor} - Unidades: {quantidade} disponíveis")
      

# Se o usuário escolher remover um livro, o programa deverá pedir o título do livro a ser removido e, caso ele exista, o livro será removido do dicionário. Se o livro não existir, o programa exibirá uma mensagem de erro.
def remover_livro(biblioteca):
    print("LIVROS PARA REMOVER")
    print(listar_livros(biblioteca))
    titulo = input("Digite o titulo do Livro: ")
    if titulo not in biblioteca:
        print("Livro não encontrado.")
    else:
        del biblioteca[titulo]
        print("\n=== REMOVER ===")
        print("===================================")
        print(f"{titulo} removido com sucesso.")
    


# Para atualizar a quantidade de livros, o programa pedirá o título do livro e a nova quantidade de exemplares. Se o livro existir, a quantidade será atualizada. Caso contrário, será exibida uma mensagem de erro.
def Atualizar_quantidade_livros(biblioteca):
    titulo = input("Digite o titulo do Livro: ")
    if titulo not in biblioteca:
        print("Livro não encontrado.")
    else:
        nova_quantidade = int(input("Digite a nova quantidade de exemplares: "))
        biblioteca[titulo]["Quantidade"] = nova_quantidade
        autor = biblioteca[titulo]["Autor"]
        print("\n=== ATUALIZAÇÃo DE EXEMPLARES ===")
        print(f" Livro: {titulo} - Autor: {autor} - Unidades: {nova_quantidade} disponíveis")



# Ao registrar um empréstimo, o programa pedirá o título do livro e a quantidade de exemplares a ser emprestada. Se houver exemplares suficientes disponíveis, a quantidade do livro será atualizada e o empréstimo será registrado. Se não houver exemplares suficientes, o programa exibirá uma mensagem de erro.
def registrar_emprestimo(biblioteca, historico_emprestimos):
    titulo = input("Digite o titulo do Livro: ")
    if titulo not in biblioteca:
        print("Livro não encontrado.")
    else:
        quantidade = int(input("Digite a quantidade de exemplares a serem emprestados: "))
        if quantidade > biblioteca[titulo]["Quantidade"]:
            print("Não há exemplares suficientes disponíveis.")
        else:
            biblioteca[titulo]["Quantidade"] -= quantidade
            print("\n=== RIGISTRO DE EMPRESTIMOS ===")
            print(f"{quantidade} exemplares de {titulo} emprestados com sucesso.")
            historico_emprestimos.append({"titulo": titulo, "quantidade": quantidade})


# O histórico de empréstimos deve ser armazenado em uma lista, onde cada entrada consiste no título do livro e a quantidade de exemplares emprestados. Quando o usuário escolher exibir o histórico de empréstimos, o programa deve mostrar todas as entradas feitas.
def historico(historico_emprestimos):
    if not historico_emprestimos:
            print("Nenhum emprestimo registrado")
    
    for emprestimo in historico_emprestimos:
        print("\n=== HISTORICO DE EMPRESTIMOS ===")
        print("===================================")
        print(f"livro: {emprestimo['titulo']} - {emprestimo['quantidade']} exemplares emprestados")


# O programa deve continuar executando até que o usuário escolha a opção de sair.
# As opções do menu são:
def main():
    while True:
        print("\nMenu:")
        print("1 - Adicionar Livro")
        print("2 - Listar livros")
        print("3 - Remover livro")
        print("4 - Atualizar quantidade de livros")
        print("5 - Registrar empréstimo")
        print("6 - Exibir histórico de empréstimos")
        print("7 - Sair")

# Adicionar livro
        escolha = int(input("Escolha uma opção (1-7): \n"))
        if escolha == 1:
            adicionar_Livro(biblioteca)
            
# Listar livros
        elif escolha == 2:
            listar_livros(biblioteca)

# Remover livro
        elif escolha == 3:
            remover_livro(biblioteca)

# Atualizar quantidade de livros
        elif escolha == 4:
            Atualizar_quantidade_livros(biblioteca)

# Registrar empréstimo
        elif escolha == 5:
            registrar_emprestimo(biblioteca,historico_emprestimos)

# Exibir histórico de empréstimos
        elif escolha == 6:
            historico(historico_emprestimos)
# Sair
        elif escolha == 7:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()



