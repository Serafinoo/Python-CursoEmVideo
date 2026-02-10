from datetime import date
atual = date.today().year
ano = int(input("Em que ano você nasceu?: "))
idade = atual - ano
print(f"O atleta tem {idade} anos ")
if idade <= 9 :
    print(f"Sua categoria é Mirim")
elif idade <= 14:
    print(f"Sua categoria é Infantil")
elif idade <= 19:
    print(f"Sua categoria é Junior")
elif idade <= 25:
    print(f"Sua categoria é Sua categoria é Senior")
elif idade > 25:
    print(f"Sua categoria é Master")