s = (input("Digite o seu sexo: ")).strip().upper()[0]
while s not in "FfMm":
    s = (input("""Você digitou errado
            Tente novamente""")).strip().upper()[0]
print("Obrigado")