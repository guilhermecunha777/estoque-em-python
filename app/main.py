from database.db import criar_tabela
from repositories import produto_repository
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')    

def input_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("valor não pode ser negativo!")
                continue
            return valor
        except ValueError:
            print("por favor, insira um numero valido.")

def input_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor == "":
            print("o campo não pode ser vazio!")
        else:
            return valor

def menu():
    while True:
        limpar_tela()
        print("\n=== Sistema de Controle de Estoque ===")
        print("1️⃣  Adicionar Produto")
        print("2️⃣  Listar Produtos")
        print("3️⃣  Editar Produto")
        print("4️⃣  Deletar Produto")
        print("5️⃣  Gerar Relatório CSV")
        print("0️⃣  Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input_texto("Nome do produto: ")
            quantidade = input_int("Quantidade: ")
            caminho_foto = input_texto("Caminho da foto: ")
            produto_repository.adicionar_produto(nome, quantidade, caminho_foto)
            print("\n✅ Produto adicionado com sucesso!\n")
            input("Pressione Enter para continuar...")

        elif opcao == '2':
            produtos = produto_repository.listar_produtos()
            if not produtos:
                print("\n🚫 Nenhum produto cadastrado.\n")
            else:
                print("\n📦 Produtos em Estoque:\n")
                print(f"{'ID':<5}{'Nome':<20}{'Qtd':<10}{'Foto'}")
                print("-" * 50)
                for produto in produtos:
                    print(f"{produto.id:<5}{produto.nome:<20}{produto.quantidade:<10}{produto.caminho_foto}")
            input("\nPressione Enter para continuar...")

        elif opcao == '3':
            id = input_int("ID do produto que deseja editar: ")
            novo_nome = input_texto("Novo nome: ")
            nova_quantidade = input_int("Nova quantidade: ")
            novo_caminho_foto = input_texto("Novo caminho da foto: ")
            produto_repository.editar_produto(id, novo_nome, nova_quantidade, novo_caminho_foto)
            print("\n✅ Produto atualizado com sucesso!\n")
            input("Pressione Enter para continuar...")

        elif opcao == '4':
            id = input_int("ID do produto que deseja deletar: ")
            confirmacao = input(f"tem certeza que quer deletar o produto id {id}? (s/n): ").lower()
            if confirmacao == 's':
                produto_repository.deletar_produto(id)
                print("\n✅ Produto deletado com sucesso!\n")
            else:
                print("\n🚫 Operação cancelada.\n")
            input("Pressione Enter para continuar...")
        
        elif opcao == '5':
            from relatorios.gerador_csv import gerar_relatorio_csv
            gerar_relatorio_csv()
            input("Pressione Enter para continuar...")

        elif opcao == '0':
            print("👋 Saindo do sistema...")
            break

        else:
            print("🚫 Opção inválida. Tente novamente!")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    criar_tabela()
    menu()
