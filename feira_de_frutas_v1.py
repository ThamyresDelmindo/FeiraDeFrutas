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
    print("🍑" * 20)
    print("\n🍊 MENU DA FEIRA🍇")
    print()
    print("🍑" * 20)
    print("1 - Ver todas as frutas")
    print("2 - Adicionar uma fruta")
    print("3 - Remover uma fruta")
    print("4 - Verificar se uma fruta está na feira")
    print("5 - Mostrar quantas frutas tem na feira")
    print("6 - Mostrar a lista completa da feira")
    print("7 - Sair do programa")
    print("🍑" * 20)

    opcao = input("\nEscolha uma opção de 1 a 7: ")
    print("🍑" * 20)

    if opcao == "1":
        print("\n😀 As frutas que temos disponíveis hoje são:")
        for fruta in frutas:
            print("\n👉", fruta)
        input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")

            
    elif opcao == "2":
        nova_fruta = input("\n😀 Digite o nome da fruta que deseja adicionar: ")
        frutas.append(nova_fruta)
        print(f"{nova_fruta} agora está na feira! 😀")
        input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")

    elif opcao == "3":
        remover_fruta = input("\n🥺 Digite o nome da fruta que deseja remover: ")
        if remover_fruta in frutas:
            frutas.remove(remover_fruta)
            print(f"{remover_fruta} não está mais na feira. 🥺")
            input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")
        else: 
            print(f"{remover_fruta} não está na feira. 👻")
            input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")

    elif opcao == "4":
        fruta_verificar = input("😀 Digite o nome da fruta que deseja procurar: ")
        if fruta_verificar in frutas:
            print("Temos no menu! 😀")
            input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")
        else:
            print("Não temos no momento, mas pode pesquisar outra fruta. 👻") 
            input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")  

    elif opcao == "5":
        print(f"No momento temos {len(frutas)} frutas na feira. 😀")
        input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")

    elif opcao == "6":
        print("😀 Lista completa de frutas disponíveis:", ", ".join(frutas))
        input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")

    elif opcao == "7":
        print("😀 Programa encerrado. Volte sempre à nossa feira!")
        break
    else:
        print("Opção inválida. Tente novamente.👻")
        input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")    