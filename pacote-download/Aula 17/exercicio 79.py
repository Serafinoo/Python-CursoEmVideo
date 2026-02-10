#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. No final, 
#serão exibidos todos os valores únicos digitados, em ordem crescente.
num = list()
while True:
    valor = int(input("Digite um valor: "))
    if valor not in num:
        num.append(valor)
    else:
        print("valor duplicado")
    continuar = input("Você deseja continuar?[S/N]: ").strip().upper()
    if continuar == "N":
        break
print("Fim")
num.sort()
print(num)