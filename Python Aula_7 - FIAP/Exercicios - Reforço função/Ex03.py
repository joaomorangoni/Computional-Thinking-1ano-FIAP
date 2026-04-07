def digitos(num):
    numc = str(num)
    numc = list(numc)
    novo_num = [int(i) for i in numc]
    return sum(novo_num)

num = int(input("Insira um número: "))
print(digitos(num))