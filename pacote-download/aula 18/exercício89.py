#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
#  notas de cada aluno individualmente.
sala = []
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota1: "))
    nota2= float(input("Nota2: "))
    media = (nota1 + nota2)/2
    sala.append([nome, [nota1, nota2], media])
    continuar = str(input("Quer Continuar? ")).upper()
    if continuar == "N":
        break
print(f""" {sala}
""")