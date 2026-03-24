def fatorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num

numero = int(input("Digite um número: "))
resul = fatorial(numero)

print(f"O fatorial de {numero} é {resul}")
