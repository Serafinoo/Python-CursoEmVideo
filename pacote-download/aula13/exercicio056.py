maior = 0
maiorn = " "
menor = 0
media = 0
soma = 0
for c in range(1,5):
    nome = (input(f"Digite o nome da {c} pessoa: "))
    idade = int(input(f"Digite a idade da {c} pessoa: "))
    sexo = (input(f"Digite o sexo da {c} pessoa [M/F]: "))
    soma += idade
    c += 1
    if c > 1 and sexo in "Mm":
        maior = idade
        maiorn = nome
    if sexo in "Mm" and idade > maior:
        maior = idade
        maiorn = nome
    if c < 20 and sexo in "fF":
        menor += 1
media += idade
media = soma/4
print(f"A media de idade do grupo é {media}")
print(f"O homem mais velho é {maiorn} com {maior} anos") 
print(f"{menor} mulheres menores que vinte anos")