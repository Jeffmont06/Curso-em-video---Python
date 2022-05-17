sal=float(input("Digite seu salario atual para saber qual será seu salario com reajuste: R$"))
if sal > 1250.00:
    salreaj = (sal * 110) / 100
if sal <= 1250.00:
    salreaj = (sal * 115) / 100
print("Seu salario com reajuste de é R${:.2f}".format(salreaj))
