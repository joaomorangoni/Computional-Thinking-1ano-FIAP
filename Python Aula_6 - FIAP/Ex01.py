def soma(a,b):
    c = a + b
    return c

def sub(a,b):
    c = a - b
    return c

def mult(a,b):
    c = a * b
    return c

def  div(a,b):
    c = a / b
    return c

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Qual operação deseja realizar? ( + - x / )")

match operacao:
    case "+":
        print(f"O resultado da soma é: {soma(num1,num2)}")
    case "-":
        print(f"O resultado da subtração é: {sub(num1,num2)}")
    case "x":
        print(f"O resultado da multiplicação é: {mult(num1,num2)}")
    case "/":
        print(f"O resultado da divisão é: {div(num1,num2)}")

