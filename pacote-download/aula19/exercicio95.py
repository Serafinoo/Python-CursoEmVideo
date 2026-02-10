# Aprimore o desafio 93 para que ele funcione com vários
#  jogadores, incluindo um sistema de visualização de 
# detalhes do aproveitamento de cada jogador.
i = 0
numjog = 0
jogador = {}
time = []
while True:
    numjog += 1
    jogador["nome"] = str(input("Nome: "))
    jogador["partidas"] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    jogador["gols"] = []
    for _ in range (1, jogador["partidas"]+1):
        gols = int(input(f"Quantos gols na partida {_}? "))
        jogador["gols"].append(gols)
    jogador["total"] = sum (jogador["gols"])
    time.append(jogador.copy())
    continuar = input("Continuar [S/N] ").upper()
    while continuar not in ("S", "N"):
        continuar = input("ERRO! Digite novamente:").upper()
    if continuar == "N":
        break
print("Nome                 Gols            Total")
for m in range(0, numjog):
    print(f"""{m} {time[m]["nome"]}         {time[m]["gols"]}               {time[m]["total"]}""")
    print("")
while True:
    dados = int(input("Mostrar dados de qual jogador? (999 parar) "))
    if dados == 999:
        break
    if dados >= len(time):
        print("ERRO! Jogador inexistente")
    else:
        print(f"Levantamento do {time[dados]["nome"]}")
        for i, g in enumerate(time[dados]["gols"]):
            print(f" No jogo {i+1} fez {g} gols.")
print("FIM")   