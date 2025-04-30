#Vai estar correto se todas as letras forem maisculas



minha_string = str(input("Digite uma palavra:"))
while True:
        if minha_string.isupper():
            print("A palavra está correta")
            minha_string = str(input("Digite uma palavra:"))
            break
        elif minha_string =="SAIR":
            print("Programa encerrado")
            break
        else:
             print("A palavra está errada")
             break