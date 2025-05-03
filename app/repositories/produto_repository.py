from database.db import conectar

def buscar_todos_produtos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()
        conn.close()
        return produtos
    except Exception as e:
        raise Exception(f"Erro ao buscar produtos: {e}")

def adicionar_produto(nome, quantidade):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, quantidade) VALUES (?, ?)", (nome, quantidade))
        conn.commit()
        conn.close()
    except Exception as e:
        raise Exception(f"Erro ao adicionar produto: {e}")

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
    except Exception as e:
        raise Exception(f"Erro ao editar produto: {e}")

def deletar_produto(id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM produtos WHERE id = ?', (id,))
        conn.commit()
        conn.close()
    except Exception as e:
        raise Exception(f"Erro ao deletar produto: {e}")

def listar_produtos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, quantidade FROM produtos")
        produtos = cursor.fetchall()
        conn.close()
        return produtos
    except Exception as e:
        raise Exception(f"Erro ao listar produtos: {e}")
