import os
import shutil
import csv
from tabulate import tabulate
from database.db import conectar
from models.produto import Produto

def adicionar_produto():
    try:
        nome = input("Nome do produto: ").strip()
        quantidade = input("Quantidade: ").strip()

        if not nome or not quantidade.isdigit():
            print("🚫 Nome e quantidade são obrigatórios e válidos.")
            return

        quantidade = int(quantidade)
        if quantidade < 0:
            print("🚫 Quantidade não pode ser negativa.")
            return

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, quantidade) VALUES (?, ?)",
                    (nome, quantidade))
        conn.commit()
        conn.close()

        print("✅ Produto adicionado com sucesso!")

    except Exception as e:
        print(f"🚫 Erro ao adicionar produto: {e}")


def listar_produtos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()
        conn.close()
        
        if not produtos:
            print("nenhum produto encontrado.")
            return
        print("lista de produtos")
        print(tabulate(produtos, headers=["ID","Nome", "Quantidade","Imagem"], tablefmt="fancy_grid"))
    except Exception as e:
        print("erro ao listar produtos: {e}")

def editar_produto(id, novo_nome, nova_quantidade):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE produtos 
            SET nome = ?, quantidade = ? 
            WHERE id = ?
        """, (novo_nome, nova_quantidade, id))
        conn.commit()
        conn.close()
        print("✅ Produto atualizado com sucesso.")
    except Exception as e:
        print(f"🚫 Erro ao editar produto: {e}")


def deletar_produto(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM produtos WHERE id=?', (id,))
    conn.commit()
    conn.close()

def buscar_produto_por_nome():
    termo = input("digite o nome produto que deseja buscar: ").strip()
    
    if not termo:
        print("voce precisa digitar algum nome.")
        return
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos WHERE nome LIKE ?", ('%' + termo + '%',))
        resultados = cursor.fetchall()
        conn.cursor()
        
        if resultados:
            print("produto encontrados: ")
            print(tabulate(resultados, headers=["ID", "Nome", "Quantidade", "Imagem"], tablefmt="fancy_grid"))
        else:
            print("nenhum produto encontrado com esse nome")
    except Exception as e:
        print("erro ao buscar produto: {e}")

def gerar_relatorio_csv():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, quantidade FROM produtos")
        produto = cursor.fetchall()
        conn.close()
        
        with open("relatorio_estoque.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv
            writer.writerow(["ID", "Nome", "Quantidade"])
            writer.writerows(produto)
        
        print("relatorio gerado com sucesso: relatorio_estoque.csv")
    except Exception as e:
        print(f"erro ao gerar relatorio: {e}")
