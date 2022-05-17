from random import choice

pergunta= input("qual a sua pergunta?")
sim = input('Sim, mas só se tu parar de brincar e ir estudar')
nao = input('Não, ela não vai querer casar contigo, tu é burro e fica brincando em vez de estudar')
resposta = [sim, nao]
escolhido = choice(resposta)
print(resposta)
