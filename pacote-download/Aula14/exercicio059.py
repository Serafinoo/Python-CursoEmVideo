e = 0
maior = 0
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
while e != 5:
    maior = n1 
    if n2 > n1:
        maior = n2
    e = int(input("""   [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
                  Qual você escolhe?: """))

    if e == 1:
        print(f"A soma entre {n1} e {n2} é: {n1+n2}")
    elif e == 2:
        print(f"A multiplicação entre {n1} e {n2} é: {n1*n2}")
    elif e == 3:
        print(f"O maior número é {maior}")
    elif e == 4:
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite outro valor: "))

print("Obrigado por usar o programa")
print("Fim")

