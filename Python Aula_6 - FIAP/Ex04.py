def vogais(a):
    A = a.count("a") + a.count("A")
    E = a.count("e") + a.count("E")
    I = a.count("i") + a.count("I")
    O = a.count("o") + a.count("O")
    U = a.count("u") + a.count("U")

    return A + E + I + O + U

frase = input("Escreva uma frase: ")
total = vogais(frase)

print(f"A frase tem {total} vogais")