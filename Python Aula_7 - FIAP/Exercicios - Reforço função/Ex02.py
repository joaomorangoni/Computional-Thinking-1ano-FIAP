def tres(a,b,c):
    lista = []
    lista.append(a)
    lista.append(b)
    lista.append(c)
    return max(lista)

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite outro número: "))

print(f"O maior número digitado é {tres(a,b,c)}")