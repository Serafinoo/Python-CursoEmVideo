#Crie um programa onde 4 jogadores joguem um dado e 
# tenham resultados aleatórios. Guarde esses resultados
#  em um dicionário em Python. No final, coloque esse 
# dicionário em ordem, sabendo que o vencedor tirou o 
# maior número no dado.
import random

ranking = {"player1": 0,
           "player2": 0,
           "player3": 0,
           "player4": 0}

for _ in range(1, 4):
    ranking[f"player{_}"] = random.randint(1,6)
valoresDecrescente = sorted(ranking.items(), key=lambda item: item[1], reverse=True)    

print(f"""{valoresDecrescente[0][0]}: {valoresDecrescente[0][1]}
{valoresDecrescente[1][0]}: {valoresDecrescente[1][1]}
{valoresDecrescente[2][0]}: {valoresDecrescente[2][1]}
{valoresDecrescente[3][0]}: {valoresDecrescente[3][1]}""")