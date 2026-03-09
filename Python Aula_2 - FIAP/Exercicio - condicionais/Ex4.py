letra = input("Insira uma letra: ")
vogal = ["a", "e", "i", "o", "u"]

if letra == vogal[0] or letra == vogal[1] or letra == vogal[2] or letra == vogal[3] or letra == vogal[4]:
    print("Sua letra é uma vogal")
else:
    print("Sua letra é uma consoante")