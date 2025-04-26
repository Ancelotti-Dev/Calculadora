def obter_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Digite um número válido.")

def menu_operacoes():
    operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
    print("\nEscolha uma operação:")
    [print(f"{i + 1} - {operacao}") for i, operacao in enumerate(operacoes)]
    while True:
        escolha = input("Escolha uma operação (1-4): ").strip()
        if escolha in ["1", "2", "3", "4"]:
            return int(escolha)
        print("Escolha inválida. Tente novamente.")

def main():
    while True:
        num1 = obter_numero("Insira o primeiro número: ")
        num2 = obter_numero("Insira o segundo número: ")

        escolha = menu_operacoes()

        # Operações usando funções lambda
        operacoes = {
            1: lambda x, y: x + y,
            2: lambda x, y: x - y,
            3: lambda x, y: x * y,
            4: lambda x, y: x / y if y != 0 else None,
        }

        operacao_nome = ["Soma", "Subtração", "Multiplicação", "Divisão"][escolha - 1]

        if escolha == 4 and num2 == 0:
            print("Divisão por zero não é permitida.")
            num2 = obter_numero("Por favor, insira outro número: ")

        resultado = operacoes[escolha](num1, num2)

        print(f"O resultado da {operacao_nome} é: {resultado}")

        continuar = input("Deseja realizar outra operação? (S/N): ").strip().upper()
        if continuar != 'S'or continuar != 's':
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()