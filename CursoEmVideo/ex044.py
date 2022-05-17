print("=~~="*3)
print("Loja do Jeff")
print("=~~="*3)

valor = float(input("Qual o valor das suas compras: R$"))
print("Como deseja pagar?\n[1] À vista no dinheiro ou cheque")
print("[2] À vista no Cartão\n[3] Em até 2x no cartão\n[4] Em até 3x no catão")
pagamento = int(input("Qual a forma de pagamento? "))

if pagamento == 1:
    desc = (valor * 10)/100
    print("O valor a pagar é R${:.2f}".format(valor-desc))
elif pagamento == 2:
    desc = (valor * 5) / 100
    print("O valor a pagar é de R${:.2f}".format(valor - desc))
elif pagamento == 3:
    print("O valor a pagar é de {:.2f}".format(valor))
elif pagamento == 4:
    juros = (valor * 20)/100
    print("O vor a pagar é de {:.2f}".format(valor + juros))
