frase = str(input('Digite uma frase: ')).strip().upper()

print('a Letra A aparece {} vezes'.format(frase.count('A')))
print('o primeiro A está na posição: {}'.format(frase.find("A")+1))
print('o ultimo A está na posição: {}'.format(frase.rfind("A")+1))
