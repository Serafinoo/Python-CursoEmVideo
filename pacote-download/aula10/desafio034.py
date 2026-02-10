import math
Salario = float(input("Qual o seu salário?: "))
if Salario > 1518:
    aumento = Salario+(Salario*10/100)
else:
   aumento = Salario+(Salario*15/100)
print(f"Seu aumento é de R${aumento}")