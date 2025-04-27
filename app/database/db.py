import sqlite3

def conectar():
    return sqlite3.connect('produtos.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            caminho_foto TEXT
        );
    ''')
    conn.commit()
    conn.close()
