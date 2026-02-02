
import sqlite3

DB_NAME = "usuarios.db"

con = sqlite3.connect(DB_NAME)
cursor = con.cursor()

# Verifica se a tabela existe
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='produtos'")
tabela_existe = cursor.fetchone()

if not tabela_existe:
    print("TABELA 'produtos' NÃO EXISTE!")
else:
    print("Tabela 'produtos' existe")
    
    # Lista os produtos
    cursor.execute("SELECT id, nome, preco FROM produtos")
    produtos = cursor.fetchall()
    
    print(f"\nTotal de produtos: {len(produtos)}\n")
    
    if len(produtos) == 0:
        print("a tabela está VAZIA!")
    else:
        for p in produtos:
            print(f"ID: {p[0]} | Nome: {p[1]} | Preço: R$ {p[2]}")

con.close()
