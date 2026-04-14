# escrita
with open('arquivo.txt', 'w', encoding="UTF-8") as file:
    file.write('Olá Mundo!')

# leitura e escrita
with open('arquivo.txt', 'r+', encoding="UTF-8") as file:
    conteudo = file.read()
    file.write("\nAdicionando mais conteúdo.")

# Abrir um arquivo para anexo
with open('arquivo.txt', 'a', encoding="UTF-8") as file:
    file.write('\nMais uma linha no final do arquivo')

# leitura
with open ('arquivo.txt', 'r', encoding="UTF-8") as file: 
    conteudo = file.read()
    print(conteudo)

