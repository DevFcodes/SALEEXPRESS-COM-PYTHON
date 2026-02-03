# 🚀 SaleExpress

Sistema web desenvolvido em **Flask** para gerenciamento de usuários, com autenticação segura e controle de sessão.

---

## 📌 Funcionalidades

- ✅ Cadastro de usuários  
- 🔐 Login com senha criptografada  
- ✏️ Edição de dados do usuário  
- 🗑️ Exclusão de usuários ( em andamento ) 
- 🔒 Controle de sessão ( login/logout )
- 🛒 Carrinho funcional


---

## 🛠 Tecnologias Utilizadas

- Python  
- Flask  
- SQLite
- HTML5  
- CSS3  
- Javascript

---

## 🔐 Segurança

- Senhas armazenadas utilizando **hash** (`werkzeug.security`)
- Verificação segura no login com `check_password_hash`
- Uso de `session` para controle de autenticação e rotas protegidas

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/DevFcodes/saleexpress.git

2️⃣ Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\Activate

3️⃣ Instale as dependências
pip install flask

▶️ Executando a Aplicação

No terminal, execute:

python app.py

🌐 Acesse no Navegador
http://127.0.0.1:5000

👨‍💻 Autor

Fabricio
Curso: Desenvolvimento de Sistemas – ETEC