print("1 - Ver Perfil\n2 - Editar Perfil\n3 - Sair\n")

perfil = {
    "nome" : "João",
    "idade" : "18"
}

while True:
    opcao = int(input("Digite a opção desejada:"))
    match opcao:
        case 1:
            print("\nAbrindo perfil...")
            print(perfil)
            break
        case 2:
            print("\nEditando perfil...")
            break
        case 3:
            print("\nDesligando...")
            break
        case _:
            print("\nOpção não encontrada")