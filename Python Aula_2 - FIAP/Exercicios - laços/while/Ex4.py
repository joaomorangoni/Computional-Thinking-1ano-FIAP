num = int(input("Insira um número positivo: "))
lista = []

while num > 0:
    lista.append(num)
    num = int(input("Insira mais um número positivo: "))

print(f"A soma dos números digitados deu {sum(lista)}")