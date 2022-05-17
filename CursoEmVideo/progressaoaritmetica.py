print("=="*11)
print("PROGRESSÃO ARITMÉTICA")
print("=="*11)

primeiro = int(input("Primeiro termo: "))
razão = int(input("digite a razão: "))
decimo = primeiro + (10 - 1) * razão
for c in range (primeiro, decimo, razão):
    print("{}".format(c), end=' ->')
print("ACABOU!!!")
