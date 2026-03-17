mes = int(input("Insira o número de um mês: "))

match mes:
    case 12 | 1 | 2:
        print("Durante esse mês é verão!")
    case 3 | 4 | 5:
        print("Durante esse mês é outono!")
    case 6 | 7 | 8:
        print("Durante esse mês é inverno!")
    case 9 | 10 | 11:
        print("Durante esse mês é primavera!")
    case _:
        print("Número inválido!!!")