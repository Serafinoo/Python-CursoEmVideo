# Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.
boletim = {}
boletim["Nome"] = str(input("Digite seu nome: "))
boletim["Media"] = float(input(f"Média de {boletim["Nome"]}: "))
print(f"""Nome é igual a {boletim["Nome"]}
Média é igual a {boletim["Media"]}""")
if boletim["Media"] >= 8:
    print("Situação é igual a estavel")
else:
    print("Situação é igual a Recuperação")