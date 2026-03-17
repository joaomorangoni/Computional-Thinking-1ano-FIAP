# ====================================== EX01 ======================================
# Crie um programa em Python que verifique se uma pessoa pode entrar em um evento 
# se for maior de 18 anos.

print("------- EX01 -------") # Estou colocando essas divisórias só para melhorar a visualização na saída :)

idade = int(input("Insira sua idade: "))
if idade < 18:
    print("Você não tem idade para entrar no evento")
else:
    print("Você pode entrar no evento")
# ==================================== FIM EX01 ====================================

# ====================================== EX02 ======================================
# Crie um programa em Python que compare dois números, peça ao usuario os numeros e
# compare se eles são iguais.

print("------- EX02 -------")

n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))
if n1 == n2:
    print("Os dois números inseridos são iguais!")
else:
    print("Os dois números inseridos são diferentes.")
# ==================================== FIM EX02 ====================================

# ====================================== EX03 ======================================
# Crie um programa em Python que registre 3 notas de um aluno e determine 
# sua situação na disciplina, peça ao usuario as 3 notas e salve em uma lista, tire 
# a media e se for 7 ou maior ele passou na materia.

print("------- EX03 -------")

notas = []
notas.append(int(input("Insira sua nota de portugues: ")))
notas.append(int(input("Insira sua nota de matemática: ")))
notas.append(int(input("Insira sua nota de ciencias: ")))

media = sum(notas) / 3

print(f"Sua média é {media:.1f}")

# ==================================== FIM EX03 ====================================

# ====================================== EX04 ======================================
# Crie um programa em Python que registre 5 produtos comprados em um mercado. 
# Use Listas, laço for e inputs.
print("------- EX04 -------")

disponivel = ["leite", "maçã", "macarrão", "queijo", "presunto"]
comprado = []
print("ID dos produtos:\n 1 - Leite\n 2 - Maçã\n 3 - Macarrão\n 4 - Queijo\n 5 - Presunto")
for i in range(1,6):
    id = int(input("digite o id dos produtos comprados: "))
    match id:
        case 1:
            comprado.append(disponivel[0])
        case 2:
            comprado.append(disponivel[1])
        case 3:
            comprado.append(disponivel[2])
        case 4:
            comprado.append(disponivel[3])
        case 5: 
            comprado.append(disponivel[4])
        case _:
            print("id não encontrado")  

print(f"Os produtos comprados são: {comprado}")
# ==================================== FIM EX04 ====================================

# ====================================== EX05 ======================================
# Crie um programa em Python que registre 5 números digitados pelo usuário e 
# depois mostre algumas informações sobre eles, use laço For.
# 1 - A lista completa de números
# 2 - O maior número
# 3 - O menor número
# 4 - A soma de todos os números

print("------- EX05 -------")
numeros = []
for i in range(1,6):
    numeros.append(int(input("Digite um número: ")))
print("-----------------------------------")
print(f"Os números são: {numeros}")
print(f"O maior número é: {max(numeros)}")
print(f"O menor número é {min(numeros)}")
print(f"A soma dos números é {sum(numeros)}")



# ==================================== FIM EX05 ====================================

# ====================================== EX06 ======================================
# Crie um programa em Python que peça números ao usuário e some todos eles.
# Use o laço while e receba numeros ate que uma condição seja atendida.
print("------- EX06 -------")

num = int(input("Insira um número positivo: "))
lista = []

while num > 0:
    lista.append(num)
    num = int(input("Insira mais um número positivo (negativo para encerrar): "))
print(f"A soma dos números digitados deu {sum(lista)}")

# ==================================== FIM EX06 ====================================

# ====================================== EX07 ======================================
# Crie um programa em Python que simule um sistema simples de login.
# Usar um primeiro laço while para pedir o nome de usuário até que 
# o usuário digite o valor correto, faça o mesmo para a senha.
print("------- EX07 -------")
email = "joao@email.com"
senha = 1001
uemail = input("Digite seu email: ")

while uemail != email:
    print("Email não existe! Tente novamente")
    uemail = input("Digite seu email: ")

usenha = int(input("Digite sua senha: "))
while usenha != senha:
    print("Senha incorreta! Tente novamente")
    usenha = int(input("Digite sua senha: "))

print("Usuário logado!")
# ==================================== FIM EX07 ====================================

# ====================================== EX08 ======================================
# Crie um programa em Python que registre 3 notas de alunos, garantindo que 
# cada nota seja válida, use as estruturas de laço for e while.
print("------- EX08 -------")
notas = []

for i in range (1,4):
    valida = False
    nota = 0
    while valida == False:
        nota = float(input("insira a nota do aluno: "))
        if nota > 0 and nota < 11:
            notas.append(nota)
            valida = True
        else:
            print("Insira uma nota válida")

print(f"As notas dos alunos são {notas:.1f}")

# ==================================== FIM EX08 ====================================

# ====================================== EX09 ======================================
# Crie um programa em Python que registre números digitados pelo usuário e 
# conte quantos são positivos. Use o laço while para registrar todas as entradas
# depois use o laço for para percorrer toda a lista e fazer a contagem.

# ==================================== FIM EX09 ====================================

# ====================================== EX10 ======================================
# Crie um programa em Python que registre as notas de 3 alunos em 4 provas usando
# uma matriz (lista de listas), calcule a media de cada aluno.
# Use seu conhecimento de laços para cumprir a tarefa.

# ==================================== FIM EX10 ====================================