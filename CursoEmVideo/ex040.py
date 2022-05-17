nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
print("Quem tirou a nota as notas {} e {} tema a média {}".format(nota1, nota2, media))
if media > 7.0:
    print("Parabéns, você foi APROVADO.")

elif media < 5.0:
    print("Sinto muito! Você foi REPROVADO.")

else:
    print("Você terá uma segunda chance. RECUPERAÇÃO.")
 