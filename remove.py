array_salario = ["1000", "6000","2345","1200" ,"1203","3440"]

novo_salario = sorted(array_salario)

novo_salario.remove(novo_salario[0])
novo_salario.remove(novo_salario[-1])

media_salario = sum(map(int, novo_salario)) // len(novo_salario)

print(novo_salario)
print(media_salario)