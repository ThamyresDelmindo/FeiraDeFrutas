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

import logging
import os
from logging import handlers

os.makedirs("logs", exist_ok=True) #Confirmando a criação da pasta de logs caso ela não exista 

#TODO: Ver se posso mudar o nome da pasta de "logs" para "histórico" 
#TODO: Colocar os nomes existentes em ordem alfabética e uma contagem de quantos nomes estão em uso

print("Seja bem vindo(a) ao Menu Feira de Frutas.")
print()
print("Escolha um nome de cliente.")
print()
print("Esses são os nomes que já estão em uso. Evite repeti-los.")

try:
    nomes_em_uso = os.listdir("logs")
except FileNotFoundError as e:
    print(f"{str(e)}.") #rever o que isso quer dizer
    sys.exit(1) #Ver se precisa desse negócio de sys.exit

for nomes in nomes_em_uso:
    nomes_usados = os.path.splitext(nomes)
    print(nomes_usados[0])

print()

while True:
    nome = input("Digite seu nome de cliente: ").strip() #Esse strip remove espaços em branco no início e no fim da palavra

    if nome == "exit":
        print("Encerrando o programa")
        break
    elif nome == "":
        print("Você precisa digitar um nome para continuar. Para encerrar o programa a qualquer momento, digite 'exit'.")
        continue
    elif os.path.exists(f"logs/{nome}.log"):
        confirma_nome_existente = input(
            f"{nome} já está em uso. Digite: \n" 
            "1 - para tentar outro nome\n"
            "2 - para continuar com o nome escolhido\n"
            "Exit - para encerrar o programa\n"    
        ).strip()
        if confirma_nome_existente == "exit":
            print("Encerrando o programa")
            break
        if confirma_nome_existente == "1":
            continue
        if confirma_nome_existente == "2":
            break
    else:
        break

#TODO: Quando dou exit, o sistema encerra o While True inicial e vai para o While True do menu da loja.
#e considera o nome que coloquei, mesmo que seja um nome já existente

log_level = getattr(logging, os.getenv("LOG_LEVEL", "INFO").upper())
log = logging.getLogger(nome)
log.setLevel(log_level)

fh = handlers.RotatingFileHandler(
    f"logs/{nome}.log", 
    maxBytes=600, #10**6 recomendado
    backupCount=10,
)

ch = logging.StreamHandler()
ch.setLevel = (log_level)

fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s ' 
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
fh.setFormatter(fmt)
ch.setFormatter(fmt)

log.addHandler(fh)
#

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
        log.info(f"{nome} escolheu a opção 1 - Ver todas as frutas")
        print("\n😀 As frutas que temos disponíveis hoje são:")
        for fruta in frutas:
            print("\n👉", fruta)
        input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")

            
    elif opcao == "2":
        nova_fruta = input("\n😀 Digite o nome da fruta que deseja adicionar: ")
        frutas.append(nova_fruta)
        log.info(f"{nome} escolheu a opção 2 - Adicionou {nova_fruta}")
        print(f"{nova_fruta} agora está na feira! 😀")
        input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")

    elif opcao == "3":
        remover_fruta = input("\n🥺 Digite o nome da fruta que deseja remover: ")
        if remover_fruta in frutas:
            frutas.remove(remover_fruta)
            log.info(f"{nome} escolheu a opção 3 - Removeu {remover_fruta}")
            print(f"{remover_fruta} não está mais na feira. 🥺")
            input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")
        else: 
            log.info(f"{nome} escolheu a opção 3 - Tentou remover {remover_fruta} mas não está na feira")
            print(f"{remover_fruta} não está na feira. 👻")
            input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")

    elif opcao == "4":
        fruta_verificar = input("😀 Digite o nome da fruta que deseja procurar: ")
        if fruta_verificar in frutas:
            log.info(f"{nome} escolheu a opção 4 - Procurou {fruta_verificar} e encontrou")
            print("Temos no menu! 😀")
            input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")
        else:
            log.info(f"{nome} escolheu a opção 4 - Procurou {fruta_verificar} e não encontrou")
            print("Não temos no momento, mas pode pesquisar outra fruta. 👻") 
            input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")  

    elif opcao == "5":
        log.info(f"{nome} escolheu a opção 5 - Ver quantidade de frutas")
        print(f"No momento temos {len(frutas)} frutas na feira. 😀")
        input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")

    elif opcao == "6":
        log.info(f"{nome} escolheu a opção 6 - Lista com todas as frutas")
        print("😀 Lista completa de frutas disponíveis:", ", ".join(frutas))
        input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")

    elif opcao == "7":
        log.info(f"{nome} escolheu a opção 7 - Sair do programa")
        print("😀 Programa encerrado. Volte sempre à nossa feira!")
        break
    else:
        log.info(f"{nome} escolheu uma opção inválida")
        print("Opção inválida. Tente novamente.👻")
        input("\n🔁 Pressione ENTER para voltar ao menu e escolher outra opção")    