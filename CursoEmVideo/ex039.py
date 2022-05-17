import datetime
nasc = int(input("Ano de nascimento: "))
print("[1] Masculino\n[2] Feminino")
sex = int(input("Qual o digito seu sexo: "))
anoatual = datetime.date.today().year
idade = anoatual - nasc
print("Quem nasceu em {} tem que {} anos em {}".format(nasc, idade, anoatual))
if idade == 18 and sex == 1:
    print("Está na hora de se alistar, vá imediatamente")
elif idade > 18 and sex == 1:
    passou = idade - 18
    print("Você já deveria ter se alistado a {} anos".format(passou))
    ano= anoatual - passou
    print("O ano que você deveria ter se alistado era: {}".format(ano))
elif idade < 18 and sex == 1:
    faltam = 18 - idade
    print("Ainda faltam {} para você se alistar".format(faltam))
    ano = anoatual + faltam
    print("O ano que você vai se alistar é: {}".format(ano))
elif idade > 18 and sex == 2:
    print("Mesmo tendo mais de 18 anos, você não precisa fazer o alisamento obrigatorio")
elif idade < 18 and sex == 2:
    print("Você ainda tem {} anos e você não precisa fazer o alisamento obrigatorio".format(idade))
