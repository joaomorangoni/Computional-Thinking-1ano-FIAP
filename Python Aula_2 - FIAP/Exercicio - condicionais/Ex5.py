qntd = int(input("Insira a quantidade de produtos comprado: "))
valor = 4.99

if qntd < 10 :
    total = valor * qntd
    print(f"O valor total deu R${total:.2f}")
else:
    desconto = (valor * qntd) / 10
    total = (valor * qntd) - desconto
    print(f"O valor total deu R${total:.2f} com desconto incluso")