try:
    divisor=(float(input("Digite um divisor: ")))
    numero = (float(input("Digite um numero: ")))
    resultado = divisor / numero
    print(resultado)
except ValueError:
    print("Error: Você não digitou um numero")

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

finally:
  print("The 'try except' is finished")
