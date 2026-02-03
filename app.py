
import sqlite3
from flask import Flask, render_template, request, redirect, session, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "senha+minha--___otarios098789-0==="


DB_NAME = "usuarios.db"

def criar_banco():
    con = sqlite3.connect(DB_NAME)  
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        endereco TEXT,
        cpf TEXT,
        data TEXT NOT NULL
    )
    """)
    con.commit()
    con.close()

criar_banco()

@app.route("/")
def home():
    if "usuarios_id" in session:
        return redirect("/catalogo")
    return redirect("/login")


@app.route("/receber", methods=["POST"])
def receber():
    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")
    endereco = request.form.get("endereco")
    data = request.form.get("data")
    cpf = request.form.get("cpf")
    
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    
    if len(cpf_limpo) != 11:
        flash("CPF inválido")
        return redirect("/form")

    if len(senha) < 4:
        flash("Senha precisa ter no mínimo 4 caracteres")
        return redirect("/form")

    senha_hash = generate_password_hash(senha)

    try:
        con = sqlite3.connect(DB_NAME) 
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha, endereco, cpf, data) VALUES (?, ?, ?, ?, ?, ?)",
            (nome, email, senha_hash, endereco, cpf_limpo, data)
        )
        user_id = cursor.lastrowid 
        con.commit()
    except Exception as e:
        flash(f"Erro ao cadastrar: {e}")
        return redirect("/form")
    finally:
        con.close()

    session["usuarios_data"] = data
    session["usuarios_end"] = endereco
    session["usuarios_id"] = user_id
    session["usuarios_nome"] = nome
    session["usuarios_email"] = email

    return redirect("/catalogo")
""""
CRUD Q TA NA SENDO UTILIZADO    

@app.route("/usuarios")
def usuarios():
    con = sqlite3.connect(DB_NAME)  
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios")
    dados = cursor.fetchall()
    con.close()
    return render_template("usuarios.html", usuarios=dados)

@app.route("/deletar/<int:id>")
def deletar(id):
    con = sqlite3.connect(DB_NAME) 
    cursor = con.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    con.commit()
    con.close()
    return redirect("/usuarios")

@app.route("/editar/<int:id>")
def editar(id):
    con = sqlite3.connect(DB_NAME)  
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    con.close()
    return render_template("editar.html", usuario=usuario)

@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):
    nome = request.form.get("nome")
    email = request.form.get("email")

    con = sqlite3.connect(DB_NAME)  
    cursor = con.cursor()
    cursor.execute(
        "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?",
        (nome, email, id)
    )
    con.commit()
    con.close()
    return redirect("/usuarios")

"""

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email")
    senha = request.form.get("senha")

    if not email or not senha:
        flash("Email e senha são obrigatórios")
        return redirect("/login")

    con = sqlite3.connect(DB_NAME)  
    cursor = con.cursor()
    cursor.execute(
        "SELECT id, nome, email, endereco, senha, data FROM usuarios WHERE email = ?",
        (email,)
    )
    usuario = cursor.fetchone()
    con.close()

    if usuario and check_password_hash(usuario[4], senha):
        session["usuarios_id"] = usuario[0]
        session["usuarios_nome"] = usuario[1]
        session["usuarios_email"] = usuario[2]
        session["usuarios_end"] = usuario[3]
        session["usuarios_data"] = usuario[5]  

        return redirect("/catalogo")
    
    flash("Email ou senha incorretos")
    return redirect("/login")


@app.route("/catalogo")
def catalogo():
    if "usuarios_id" not in session:
        return redirect("/login")

    return render_template(
        "catalogo.html",
        nome=session.get("usuarios_nome", ""),
        email=session.get("usuarios_email", "")
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/userSale")
def userSale():
    if "usuarios_id" not in session:
        return redirect("/login")

    return render_template(
        "userSale.html",
        nome=session.get("usuarios_nome", ""),
        email=session.get("usuarios_email", ""),
        data=session.get("usuarios_data", ""),
        endereco=session.get("usuarios_end", "")
    )

@app.route("/config")
def config():
    if "usuarios_id" not in session:
        return redirect("/login")

    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()

    cursor.execute(
        """
        SELECT nome, email, data, endereco
        FROM usuarios
        WHERE id = ?
        """,
        (session["usuarios_id"],)
    )

    usuario = cursor.fetchone()
    con.close()

    if not usuario:
        session.clear()
        return redirect("/login")

    return render_template(
        "config.html",
        nome=usuario[0],
        email=usuario[1],
        data=usuario[2],
        endereco=usuario[3]
    )

@app.route("/config/editar", methods=["POST"])
def editar_config():
    if "usuarios_id" not in session:
        return redirect("/login")

    nome = request.form.get("nome")
    email = request.form.get("email")
    endereco = request.form.get("endereco")
    
    if not nome:
        flash ("O nome não pode ficar vazio")
        return redirect("/config")

    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()

    cursor.execute(
        """
        UPDATE usuarios
        SET nome = ?, email = ?, endereco = ?
        WHERE id = ?
        """,
        (nome, email, endereco, session["usuarios_id"])
    )

    con.commit()
    con.close()
    
    
    session["usuarios_nome"] = nome
    session["usuarios_email"] = email
    session["usuarios_end"] = endereco

    flash("Dados atualizados com sucesso!")
    return redirect("/config")


@app.route("/config/deletar", methods=["POST"])
def deletar_conta():
    if "usuarios_id" not in session:
        return redirect("/login")

    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()

    cursor.execute(
        "DELETE FROM usuarios WHERE id = ?",
        (session["usuarios_id"],)
    )

    con.commit()
    con.close()

    session.clear()
    return redirect("/login")


@app.route("/produto/<int:id>")
def produto(id):
    if "usuarios_id" not in session:
        return redirect("/login")
    
    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()
    
    cursor.execute("""
        SELECT id, nome, descricao, preco, imagem
        FROM produtos
        WHERE id = ?
    """, (id,))
    
    produto = cursor.fetchone()
    con.close()
    
    if not produto:
        flash("Produto não encontrado")
        return redirect("/catalogo")
    
    
    produto_dict = {
        'id': produto[0],
        'nome': produto[1],
        'descricao': produto[2],
        'preco': produto[3],
        'imagem': produto[4]
    }
    
    return render_template(
        "produto.html",
        produto=produto_dict  
    )
    
@app.route("/add_carrinho/<int:produto_id>", methods=["POST", "GET"])
def add_carrinho(produto_id):
    if "usuarios_id" not in session:
        return redirect("/login")
    
    if "carrinho" not in session:
        session["carrinho"] = []
    
    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()
    cursor.execute("SELECT id, nome, preco, imagem FROM produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()
    con.close()
    
    if produto:
        produto_existe = False
        for item in session["carrinho"]:
            if item['id'] == produto_id:
                item['qtd'] += 1
                produto_existe = True
                break
        
        if not produto_existe:
            session["carrinho"].append({
                'id': produto[0],
                'nome': produto[1],
                'preco': produto[2],
                'imagem': produto[3],
                'qtd': 1
            })
        
        session.modified = True
        flash(f"{produto[1]} adicionado ao carrinho!")
    else:
        flash("Produto não encontrado")
    
    return redirect(url_for("produto", id=produto_id))

            
    
    
@app.route("/carrinho")
def carrinho():
    if "usuarios_id" not in session:
        return redirect("/login")
    
    carrinho = session.get("carrinho", [])
    
    total = sum(item['preco'] * item['qtd'] for item in carrinho)
    
    return render_template(
        "carrinho.html",
        carrinho=carrinho,
        total=total
    )
    
@app.route("/remover_carrinho/<int:produto_id>")
def remover_carrinho(produto_id):
    if "usuarios_id" not in session:
        return redirect("/login")
    
    if "carrinho" in session:
        session["carrinho"] = [
            item for item in session["carrinho"] 
            if item['id'] != produto_id
        ]
        session.modified = True
        flash("Item removido do carrinho")
    
    return redirect("/carrinho")
    
@app.route("/atualizar_quantidade/<int:produto_id>/<acao>")
def atualizar_quantidade(produto_id, acao):
    if "usuarios_id" not in session:
        return redirect("/login")
    
    if "carrinho" in session:
        for item in session["carrinho"]:
            if item['id'] == produto_id:
                if acao == "aumentar":
                    item['qtd'] += 1
                elif acao == "diminuir" and item['qtd'] > 1:
                    item['qtd'] -= 1
                break
        
        session.modified = True
    
    return redirect("/carrinho")
    
    
@app.route("/chat")
def chat():
    if "usuarios_id" not in session:
        return redirect("/login")

    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()

    cursor.execute(
        """
        SELECT nome, email, data, endereco
        FROM usuarios
        WHERE id = ?
        """,
        (session["usuarios_id"],)
    )

    usuario = cursor.fetchone()
    con.close()

    if not usuario:
        session.clear()
        return redirect("/login")

    return render_template(
        "chat.html",
        nome=usuario[0]
    )



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)