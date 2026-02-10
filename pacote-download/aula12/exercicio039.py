ano = int(input("Em que ano você nasceu?: "))
idade = 2025 - ano
if idade < 18:
    print(f"Você tem {idade} anos, falta(m) {18-idade} ano(s) para seu alistamento ")
elif idade == 18:
    print(f"Você tem {idade} anos, você deve se alistar ao exercito")
elif idade > 18:
    print(f"Você tem {idade} anos, seu tempo de se alistar no exercito já passou à {idade-18} anos")