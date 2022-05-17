valorcasa = float(input("qual o valor da casa que deseja comprar? R$"))
salario = float(input("Qual o seu sálario? R$"))
tempoano = int(input("Em quantos anos deseja pagar? "))
tempomes = tempoano * 12
prestacao = valorcasa / tempomes
parsal = (salario*30)/100
if parsal >= prestacao:
    print("O emprestimo pode ser consedido!")
    print("a parcela será de {}x de R${:.2f}".format(tempomes,prestacao))
else:
    print("O emprestimo não pode ser consedido!")
