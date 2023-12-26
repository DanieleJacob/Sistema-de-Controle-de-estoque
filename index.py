estoque = []
opcao = 0

# FUNÇÕES

def menu():
    print("-------------------------------")
    print("Sistema de Controle de estoque")
    print("-------------------------------")
    print("[1] - Adicionar produto")
    print("[2] - Listar produtos")
    print("[3] - Editar produto")
    print("[4] - Excluir produto")
    print("[5] - Sair")
    print("-------------------------------")
    print("\n")

# Função adicionar produtos
def adicionar(nome, quantidade):
    produto = {"nome": nome, "quantidade": quantidade}
    estoque.append(produto)

# Função listar produtos
def listar():
    if not estoque:
        print("Não existem produtos no estoque")
        print("\n")
    else:
        for indice, produto in enumerate(estoque):
            print(f'Índice: {indice}')
            print(f'Nome: {produto["nome"]}')
            print(f'Quantidade: {produto["quantidade"]}')
            print("\n")

#Função editar produtos

def editar(editar_produto, nome, quantidade):
    for produto in estoque:
        if produto["nome"] == editar_produto:
            produto["nome"] = nome
            produto["quantidade"] = quantidade
            print("-------------------------------")
            print("Produto editado com sucesso!")
            print("\n")
        else:
          print("-------------------------------")
          print("Produto não existe no estoque")
          print("/n")

# Função excluir produto
def excluir(excluir_nome):
    for produto in estoque:
        if produto["nome"] == excluir_nome:
            estoque.remove(produto)
            print("-------------------------------")
            print("Produto excluído com sucesso!")
            print("\n")
            return
    print("-------------------------------")
    print("Produto não encontrado no estoque")
    print("\n")

while opcao != 5:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("[1] - Adicionar produto")
        print("-------------------------------")
        nome = input("Digite o nome do produto: ")
        quantidade = input("Digite a quantidade do produto: ")
        adicionar(nome, quantidade)
        print("\n")

    if opcao == 2:
        print("[2] - Listar produtos")
        print("-------------------------------")
        print("\n")
        listar()

    if(opcao==3):
      print("[3] - Editar produto")
      print("-------------------------------")

      editar_produto = input("Qual produto deseja editar? ")
      nome = input("-> Informe o novo nome: ")
      quantidade = input("-> Informe a nova quantidade: ")

      editar(editar_produto, nome,quantidade)

    if opcao == 4:
        print("[4] - Excluir produto")
        print("-------------------------------")
        excluir_nome = input("Informe o nome do produto: ")
        excluir(excluir_nome)

    if opcao == 5:
        print("Fim do programa")
        break
