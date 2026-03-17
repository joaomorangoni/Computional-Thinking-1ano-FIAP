nota = int(input("Insira a nota do aluno: "))
match nota:
    case 10 | 9:
        print("O aluno foi excelente!")
    case 7 | 8:
        print("O aluno foi bem")
    case 5 | 6:
        print("O aluno foi regular")
    case i if i < 5 and i >= 0:
        print("O aluno foi reprovado!")
    case _:
        print("Insira uma nota válida!")
