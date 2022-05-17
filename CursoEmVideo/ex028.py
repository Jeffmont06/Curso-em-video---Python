import random
print(str("Eu pensei em um numero entre 0 e 5. Tente advinhar..."))
pc = random.randint(0, 5)
usuario = int(input("Em que numero eu pensei? "))
if usuario == pc:
    print('Você ganhou. Parabens!!')
else:
    print("Perdeu!! O numero que eu pensei foi {} e não {}".format(pc, usuario))
