print('=={}=='* 4)
print("Analizador de Triangulos")
print('=={}=='* 4)

c1= float(input("Digite o primeiro Segmento: "))
c2= float(input("Digite o segundo segmento: "))
c3= float(input("Digite o terceiro segmento: "))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print("Os Segmentos a cima podem formar um triangulo")
else:
    print("Os segmentos a cima não podem formar um triangulo")
