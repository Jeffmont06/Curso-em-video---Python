k = float(input("Quantos km foram rodados com o carro? "))
d = int(input("Por quantos dias o veiculo foi alugado? "))
kmc = (k * 0.15)+(d*60)
print("O valor a se pagar é de R${:.2f}".format(kmc))
