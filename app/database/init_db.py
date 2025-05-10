import sqlite3
import os

# Caminho absoluto do banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', '..', 'estoque.db')

def inicializar_banco():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                imagem TEXT
            )
        """)

        conn.commit()
        conn.close()
        print("✅ Banco de dados inicializado com sucesso.")
    except sqlite3.Error as e:
        print(f"🚫 Erro ao inicializar banco de dados: {e}")

if __name__ == "__main__":
    inicializar_banco()
