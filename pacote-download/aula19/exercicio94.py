galera = []
pessoas = {}
soma = 0
idades = 0 
mulheres = 0
while True:
    pessoas["nome"] = input("Nome: ")
    pessoas["sexo"] = input("Sexo: ").upper()
    if pessoas["sexo"] not in ("M", "F"):
        pessoas["sexo"] = input("ERRO! Digite novamente: ").upper()
    if pessoas["sexo"] == "F":
        mulheres += 1
    pessoas["idade"] = int(input("Idade: "))
    idades += 1
    soma += pessoas["idade"]
    media = soma / idades
    galera.append(pessoas.copy())
    continuar = input("Continuar [S/N] ").upper()
    if continuar not in ("S", "N"):
        continuar = input("ERRO! Digite novamente: ")
    if continuar == "N":
        break
print(f""" A)Foram cadastradas ao total {len(galera)}
B) A média de idade foi {media}
C) Foram Cadastradas ao todo {mulheres} mulheres
D) As pessoas com idade acima da média são:""")
for p in galera:
    if p["idade"] >= media:
        for k, v in p.items():
            print(f"    {k} = {v};", end=" ")
print("FIM")