dis = float(input("Qual a distancia da sua viagem em Km? "))
if dis <= 200:
    valor1 = float(dis*0.5)
    print("O valor a pagar é de R${:.2f}".format(valor1))
else:
    valor2 = float(dis*0.48)
    print("O valor promocional da viagem é: R${:.2f}".format(valor2))
