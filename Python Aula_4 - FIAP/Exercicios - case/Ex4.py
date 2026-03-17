idade = int(input("insira sua idade: "))

match idade:
    case i if i > 0 and i <= 12:
        print("Você é uma criança.")
    case i if i >= 13 and i < 18:
        print("Você é adolescente.")
    case i if i >= 18:
        print("Você é adulto.")
    case _: 
        print("Idade inválida!")
        