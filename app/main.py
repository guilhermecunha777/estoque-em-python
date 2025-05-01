from repositories import produto_repository
from database.db import criar_tabela
import os

def menu():
    while True:
        print("\n" + "=" * 40)
        print("🧠 SISTEMA DE CONTROLE DE ESTOQUE 🧠")
        print("=" * 40)
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Deletar produto")
        print("4. Buscar produto por nome")
        print("6. Editar produto")
        print("5. Gerar relatório CSV")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            produto_repository.adicionar_produto()

        elif opcao == "2":
            produto_repository.listar_produtos()

        elif opcao == "3":
            id_produto = input("digite o ID do produto que deseja deletar: ").strip()
            if id_produto.isdigit():
                produto_repository.deletar_produto(int(id_produto))
                print("item deletado")
            else:
                print("ID invalido")

        elif opcao == "4":
            produto_repository.buscar_produto_por_nome()

        elif opcao == "5":
            produto_repository.gerar_relatorio_csv()

        elif opcao == "6":
            id_produto = input("Digite o ID do produto que deseja editar: ").strip()
            if id_produto.isdigit():
                novo_nome = input("Novo nome do produto: ").strip()
                nova_quantidade = input("Nova quantidade: ").strip()
                if not nova_quantidade.isdigit():
                    print("🚫 Quantidade inválida.")
                    return
                produto_repository.editar_produto(
                    int(id_produto),
                    novo_nome,
                    int(nova_quantidade))
            else:
                print("🚫 ID inválido.")


        elif opcao == "0":
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("🚫 Opção inválida. Tente novamente.")

if __name__ == "__main__":
    criar_tabela()
    menu()
