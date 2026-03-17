dia = int(input("Insira um número de 1 a 7: "))

match dia:
    case 1:
        print("Seu dia será domingo!")
    case 2:
        print("Seu dia será segunda!")
    case 3:
        print("Seu dia será terça!")
    case 4:
        print("Seu dia será quarta!")
    case 5:
        print("Seu dia será quinta!")
    case 6:
        print("Seu dia será sexta!")
    case 7:
        print("Seu dia será sábado!")
    case _:
        print("Número inválido!!")