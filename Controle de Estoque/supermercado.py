import mysql.connector

# Conectando ao banco de dados
conexao = mysql.connector.connect(
    host="localhost",  # Endereço do servidor
    user="root",       # Usuário MySQL
    password="123",  # Senha do MySQL
    database="supermercado"
)

cursor = conexao.cursor()

# Funções do sistema
def adicionar_produto():
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    cursor.execute(
        "INSERT INTO produtos (nome, categoria, quantidade, preco) VALUES (%s, %s, %s, %s)",
        (nome, categoria, quantidade, preco)
    )
    conexao.commit()
    print("Produto adicionado com sucesso!")

def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    print("\n--- Estoque Atual ---")
    for produto in produtos:
        print(f"ID: {produto[0]}, Nome: {produto[1]}, Categoria: {produto[2]}, Quantidade: {produto[3]}, Preço: R${produto[4]:.2f}")
    print("--------------------\n")

def atualizar_produto():
    id_produto = int(input("ID do produto para atualizar: "))
    nova_quantidade = int(input("Nova quantidade: "))
    novo_preco = float(input("Novo preço: "))
    cursor.execute(
        "UPDATE produtos SET quantidade = %s, preco = %s WHERE id = %s",
        (nova_quantidade, novo_preco, id_produto)
    )
    conexao.commit()
    print("Produto atualizado com sucesso!")

def remover_produto():
    id_produto = int(input("ID do produto para remover: "))
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
    conexao.commit()
    print("Produto removido com sucesso!")

def buscar_produto():
    nome_produto = input("Nome do produto para buscar: ")
    cursor.execute("SELECT * FROM produtos WHERE nome LIKE %s", (f"%{nome_produto}%",))
    produtos = cursor.fetchall()
    print("\n--- Resultado da Busca ---")
    for produto in produtos:
        print(f"ID: {produto[0]}, Nome: {produto[1]}, Categoria: {produto[2]}, Quantidade: {produto[3]}, Preço: R${produto[4]:.2f}")
    print("--------------------------\n")

# Menu principal
while True:
    print("\n--- Controle de Estoque ---")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Produto")
    print("4. Remover Produto")
    print("5. Buscar Produto")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        atualizar_produto()
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        buscar_produto()
    elif opcao == "6":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Fechar
cursor.close()
conexao.close()