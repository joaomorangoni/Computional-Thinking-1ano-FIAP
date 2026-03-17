import random

tentativas = 3
resposta = random.randint(1,10)
escolha = int(input("Insira um número de 1 a 10: "))

while tentativas >= 1 and escolha != resposta:
    tentativas = tentativas - 1
    print("Resposta errada! Tente novamente")
    print(f"Sobraram {tentativas} chances")
    escolha = int(input("Insira um número de 1 a 10: "))

if tentativas == 0:
    print("Você não conseguiu")
if escolha == resposta:
    print("Você acertou!!!")
