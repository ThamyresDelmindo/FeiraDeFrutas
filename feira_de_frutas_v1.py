# Projeto: Feira de Frutas

# Objetivo: Criar um programa que simula uma feira de frutas, onde:
# - Existe uma lista de frutas disponíveis para venda.
# - O cliente pode ver as frutas, adicionar novas frutas na feira,
#   remover frutas, verificar se uma fruta existe e saber quantas frutas tem na feira.

# Projeto: Feira de Frutas

# Objetivo: Criar um programa que simula uma feira de frutas, onde:
# - Existe uma lista de frutas disponíveis para venda.
# - O cliente pode ver as frutas, adicionar novas frutas na feira,
#   remover frutas, verificar se uma fruta existe e saber quantas frutas tem na feira.

# Passo 1 - Crie uma lista chamada "feira" com 5 frutas que você escolher.

# Passo 2 - Mostre um menu de opções para o usuário:
# 1 - Ver todas as frutas da feira
# 2 - Adicionar uma fruta na feira
# 3 - Remover uma fruta da feira
# 4 - Verificar se uma fruta está na feira
# 5 - Mostrar quantas frutas tem na feira
# 6 - Mostrar a lista completa da feira
# 7 - Sair do programa

# Passo 3 - O programa deve rodar em loop até o usuário escolher sair (opção 7).

# Passo 4 - Cada opção do menu executa uma ação com a lista de frutas.

# Desafio bônus: Deixar o programa bonitinho, com mensagens explicativas.


frutas = ["Laranja", "Manga", "Banana", "Uva", "Goiaba"]
while True:
    print("\n🍊 MENU DA FEIRA🍇")
    print("1 - Ver todas as frutas")
    print("2 - Adicionar uma fruta")
    print("3 - Remover uma fruta")
    print("4 - Verificar se uma fruta está na feira")
    print("5 - Mostrar quantas frutas tem na feira")
    print("6 - Mostras a lista completa da feira")
    print("7 - Sair do programa")

    opcao = input("Escolha uma opção (1 a 7): ")

    if opcao == "1":
        print("\nAs frutas que temos disponíveis hoje são:")
        for fruta in frutas:
            print("-", fruta)

    elif opcao == "2":
        nova_fruta = input("Digite o nome da fruta que deseja adicionar: ")
        frutas.append(nova_fruta)
        print(f"{nova_fruta} foi adicionada à feira!")

    elif opcao == "3":
        remover_fruta = input("Digite o nome da fruta que deseja remover: ")
        if remover_fruta in frutas:
            frutas.remove(remover_fruta)
            print(f"{remover_fruta} foi removida da feira.")
        else: 
            print(f"{remover_fruta} não está na feira")

    elif opcao == "4":
        fruta_verificar = input("Digite o nome da fruta que deseja procurar: ")
        if fruta_verificar in frutas:
            print("Temos no menu!")
        else:
            print("Não temos no momento, mas pode procurar outra fruta.")   

    elif opcao == "5":
        print(f"No momento temos {len(frutas)} frutas na feira.")

    elif opcao == "6":
        print("Lista completa:", frutas)

    elif opcao == "7":
        print("Programa encerrado. Volte sempre à nossa feira!")
        break
    else:
        print("Opção inválida. Tente novamente.")    