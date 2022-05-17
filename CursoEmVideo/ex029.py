vel = int(input("Qual a velocidade atingida? "))

if vel <= 80:
    print("Dirija com segurança!")
else:
    multa = float((vel - 80)*7)
    print("Você foi multado!! O valor a pagar é de R${:.2f}".format(multa))
    