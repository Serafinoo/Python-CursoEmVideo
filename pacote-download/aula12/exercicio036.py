valor = float(input("Qual o valor da casa?: "))
salario = float(input("Qual o seu salário?: "))
anos = float(input("Em quantos anos você vai pagar?: "))
prest = (anos*12)/valor
limite = salario*30/100
if prest <= limite:
    print("Emprestimo aprovado")
else:
    print("Emprestimo negado")