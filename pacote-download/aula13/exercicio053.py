frase = (input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
invertido = ""
for letra in range(len(junto) -1, -1, -1):
    invertido += junto[letra]
print(junto,invertido)
if invertido == junto:
    print("Temos um palindromo!")
else:
    print("Não é um palindromo")