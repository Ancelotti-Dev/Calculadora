# try:
#     divisor=(float(input("Digite um divisor: ")))
#     numero = (float(input("Digite um numero: ")))
#     resultado = divisor / numero
#     print(resultado)

# except ValueError:
#     print("Error: Você não digitou um numero")

# except ZeroDivisionError:
#     print("Erro: Divisão por zero não é permitida.")

# finally:
#   print("The 'try except' is finished")


import os
# Aqui eu fiz um try e except para abrir o arquivo .url do Counter-Strike 2, e depois eu usei o os.startfile para abrir o arquivo via Steam
# isso vai abrir via Steam, e não via navegador, e eu coloquei o caminho do arquivo .url que eu quero abrir
try:
    with open(r"C:\Users\Ancelotti\OneDrive\Desktop\Counter-Strike 2.url", "r") as file:
        for linha in file:
            if linha.startswith("URL="):
                url = linha.strip().split("=", 1)[1]
                os.startfile(url)  # isso vai abrir via Steam!
except FileNotFoundError:
    print("error: Arquivo não encontrado")