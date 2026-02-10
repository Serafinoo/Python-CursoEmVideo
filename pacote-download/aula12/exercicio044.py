preco = float(input("Preço das compras: "))
pag = int(input("""Formas de pagamento
[1] A vista dinheiro/cheque
[2] A vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual você vai escolher?: """))
if pag == 1:
    desconto = preco-(10*preco/100)
    print(f"O preço das suas compras é de {preco} mas você vai pagar {desconto}")
elif pag == 2:
    desconto = preco-(5*preco/100)
    print(f"O preço das suas compras é de {preco} mas você vai pagar {desconto}")
elif pag == 3:
    print(f"Você vai pagar {preco} em 2x no cartão")
elif pag == 4:
    desconto = preco+(20*preco/100)
    print(f"O preço das suas compras é de {preco} mas você vai pagar {desconto}")