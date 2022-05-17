frase = str(input("Qual o seu nome completo? ").strip())

print("Seu nome completamente maiusculo é: {}".format(frase.upper()))
print('Seu nome completamente minusculas é: {}'.format(frase.lower()))

print("Seu nome completo tem {} letras".format(len(frase.replace(" ",""))))

print("Seu primeiro nome tem {} letras".format(frase.find(' ')))
