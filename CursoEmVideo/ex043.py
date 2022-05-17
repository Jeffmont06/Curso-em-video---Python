peso = float(input("Qual seu peso: (Kg)"))
alt = float(input("Qual sua altura: (m)"))
imc = float(peso / (alt**2))
print("Seu IMC é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está ABAIXO DO PESO")
elif 18.5 < imc < 25.0:
    print("Você está com o PESO IDEAL")
elif 25.0 < imc < 30.0:
    print("Você está com SOBREPESO")
elif 30.0 < imc < 40.0:
    print("Cuidado! Você está OBESO")
elif imc > 40.0:
    print("Você vai precisar de um caixão bem maior")
