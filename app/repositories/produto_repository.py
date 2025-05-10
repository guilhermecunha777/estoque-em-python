from app.schemas import produto_schema
from app.database import conectar


def listar_produtos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, quantidade, imagem FROM produtos")
        produtos_raw = cursor.fetchall()
        conn.close()

        produtos = []
        for prod in produtos_raw:
            produtos.append({
                "id": prod[0],
                "nome": prod[1],
                "quantidade": prod[2],
                "imagem": prod[3]
            })
        return produtos
    except Exception as e:
        raise Exception(f"Erro ao listar produtos: {e}")

def adicionar_produto(nome: str, quantidade: int):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, quantidade) VALUES (?, ?)", (nome, quantidade))
        conn.commit()
        produto_id = cursor.lastrowid
        conn.close()

        return {
            "id": produto_id,
            "nome": nome,
            "quantidade": quantidade,
            "imagem": None
        }
    except Exception as e:
        raise Exception(f"Erro ao adicionar produto: {e}")

def editar_produto(id: int, nome: str, quantidade: int):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE produtos SET nome = ?, quantidade = ? WHERE id = ?", (nome, quantidade, id))
        conn.commit()
        conn.close()

        return {
            "id": id,
            "nome": nome,
            "quantidade": quantidade,
            "imagem": None
        }
    except Exception as e:
        raise Exception(f"Erro ao editar produto: {e}")

def deletar_produto(id: int):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        conn.commit()
        conn.close()
    except Exception as e:
        raise Exception(f"Erro ao deletar produto: {e}")

def buscar_todos_produtos():
    return listar_produtos()
