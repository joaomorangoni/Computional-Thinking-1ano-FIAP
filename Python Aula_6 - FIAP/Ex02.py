def primo(n):
    lista = []
    for i in range (1,n+1):
        lista.append(n % i)
    if lista.count(0) == 2:
        return True
    else:
        return False
    
num = int(input("Digite um número: "))
if primo(num) == True:
    print("O número é primo!!")
else:
    print("O número não é primo")
