def media(lista):
    media = (sum(lista))/len(lista)
    return media

numeros = []
while True:
    num = int(input("Insira um número (negativo para encerrar): "))
    if num < 0:
        break
    numeros.append(num)

resul = media(numeros)

print(f"A média dos números é {resul:.2f}")