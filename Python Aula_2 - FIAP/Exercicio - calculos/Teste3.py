livro = 25
caneta = 5

qntdL = int(input("Insira a quantidade de livros que comprou:"))
qntdC = int(input("Insira a quantidade de canetas que comprou:"))

total = float((qntdL * livro) + (qntdC * caneta))

print(f"O valor total de sua compra deu: R${total:.2f}")