def palindromo(t):
    t = list(t)
    ti = []
    for i in reversed(t):
        ti.append(i)
    if ti == t:
        return True
    else:
        return False

text = input("Digite um texto: ")

if palindromo(text.replace(" ", "")):
    print("Seu texto é um palindromo")
else:
    print("Seu texto não é um palindromo")
