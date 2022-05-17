from datetime import date
nasc = int(input("Qual seu ano de nascimento: "))
ano = date.today().year
idade = ano - nasc

if idade > 25:
    print("Você tem {} anos e sua catégoria na natação é: MASTER".format(idade))
elif idade <= 9:
    print("Você tem {} anos e sua catégoria na natação é: MIRIM".format(idade))
elif idade <= 14:
    print("Você tem {} anos e sua catégoria na natação é: INFANTIL".format(idade))
elif idade <= 19:
    print("Você tem {} anos e sua catégoria na natação é: JUNIOR".format(idade))
elif idade <= 25:
    print("Você tem {} anos e sua catégoria na natação é: SENIOR".format(idade))
