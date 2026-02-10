n = 0
c = 0
soma = 0
while n != 999:
    n = int(input("Digite um número: "))
    soma += n
    c += 1
print(f"""A soma de todos os numeros que você digitou é: {soma - 999}
E o numero de vezes que você digitou foi {c}""")
print("FIM")