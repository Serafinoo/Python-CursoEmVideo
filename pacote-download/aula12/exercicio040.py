nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print("Você está aprovado!")
elif media >= 5.0 and 6.9:
    print("Você está de recuperação")
elif media < 5.0:
    print("Você está reprovado")