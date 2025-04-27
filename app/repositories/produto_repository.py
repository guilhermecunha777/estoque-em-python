import os
import shutil
from database.db import conectar
from models.produto import Produto

def adicionar_produto(nome, quantidade, caminho_foto):
    pasta_fotos = os.path.join(os.path.dirname(__file__), '..', 'fotos')
    pasta_fotos = os.path.abspath(pasta_fotos)
    if not os.path.exists(pasta_fotos):
        os.makedirs(pasta_fotos)
    
    nome_arquivo = os.path.basename(caminho_foto)
    novo_caminho_foto = os.path.join(pasta_fotos, nome_arquivo)
    
    try:
        shutil.copy2(caminho_foto, novo_caminho_foto)
    except FileNotFoundError:
        print("\n Arquivo de imagem não encontrado. Produto cadastrado sem foto.\n")
        novo_caminho_foto = ""
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO produtos (nome, quantidade, caminho_foto) VALUES (?, ?, ?)', (nome, quantidade, caminho_foto))
    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    rows = cursor.fetchall()
    conn.close()
    produtos = [Produto(id=row[0], nome=row[1], quantidade=row[2], caminho_foto=row[3]) for row in rows]
    return produtos

def editar_produto(id, novo_nome, nova_quantidade, novo_caminho_foto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE produtos
        SET nome = ?, quantidade = ?, caminho_foto = ?
        WHERE id = ?
    ''', (novo_nome, nova_quantidade, novo_caminho_foto, id))
    conn.commit()
    conn.close()

def deletar_produto(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM produtos WHERE id=?', (id,))
    conn.commit()
    conn.close()
