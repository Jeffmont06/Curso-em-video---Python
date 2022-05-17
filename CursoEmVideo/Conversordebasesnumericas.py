print("Conversor de Bases numericas")
num = int(input("Digite um numero inteiro: "))
print("[1] Binario\n[2] octal\n[3] exadecimal")
ops = int(input("Para qual tipo deseja converter?"))
if ops == 1:
    print("O valor {} em binário é {}".format(num, format(num, 'b')))
elif ops == 2:
    print(" valor {} em octal é {}".format(num, format(num, 'o')))
elif ops == 3:
    print("O valor {} em exadecimal é {}".format(num, format(num, 'x')))
else:
    print("OPÇÃO INVALIDA")
