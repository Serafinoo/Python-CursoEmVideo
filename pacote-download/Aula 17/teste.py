#FINALMENTE PRATICA
#tuplas
#num = (2, 5, 9, 1)
#num [2] = 3
#print(num)
#listas
#num = [2, 5, 9, 1]
#num[2] = 3
#num.append(7)
#num.insert(2, 0)
#num.pop(2)
#if 5 in num:
#    num.remove(5)
#else:
#    print("error")
#num.sort(reverse=True)
#print(num)
#print(f"Essa lista tem {len(num)} elementos")
valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Fim")