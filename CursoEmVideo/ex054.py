from datetime import datetime


from datetime import  date
atual = date.today().year

ano = int (input("Digite o seu ano de nascimento: "))
idade = atual - ano
print("Essa pressoa tem {} anos".format(idade))
