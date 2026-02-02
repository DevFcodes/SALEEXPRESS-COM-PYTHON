
import sqlite3

DB_NAME = "usuarios.db"

con = sqlite3.connect(DB_NAME)
cursor = con.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nome TEXT NOT NULL,
       descricao TEXT NOT NULL,
       preco REAL NOT NULL,
       imagem TEXT NOT NULL 
    )
""")

cursor.execute("""
    INSERT INTO produtos (nome, descricao, preco, imagem) VALUES
    ('Tenis Nike R7', 'Tênis Nike Revolution 7, tenis bom e confortavel.', 300.00, 'img1.jpg'),
    ('Tenis Nike A1', 'Tênis Nike Air force 1, tenis bom e confortavel.', 759.99, 'img21.jpg'),
    ('Tenis New A1', 'TENIS DO SPFC NEW 2025 TENIS 480 Low São Paulo', 400.99, 'img1.1.jpg'),
    ('Camisa Nike', 'Camisa da nike, boa, estilosa e confortavel, otima para se usar no dia a dia.', 100.00, 'img2.jpg'),
    ('Camisa SP', 'Camisa jogador do São Paulo Futebol Clube 2025', 350.00, 'img20jpg.jpg'),
    ('Jaqueta SP', 'JAQUETA DO SPFC NEW 2025', 499.99, 'jaqueta brnca.jpg'),
    ('Shorts Nike', 'Shorts da nike, bom, estiloso e confortavel, otimo para se usar no dia a dia.', 80.00, 'img3.jpg'),
    ('Teclado 63', 'Rapid Trigger Distância De Ativação (Ajustável): 0.1 Mm - 4.0 Mm', 2312.19, 'img17.jpg'),
    ('Celular 25', 'Smartphone Samsung Galaxy S24, Ultra, Galaxy AI', 6929.10, 'img5.jpg'),
    ('Monitor Tk', 'Configuração: Monitor de 21,5" Resolução FHD de 1920 x 1080 Energy Star 8.0', 865.99, 'img6.jpg'),
    ('Fone JBL', 'Fone JBL, bom e confortavel', 290.00, 'img7.jpg'),
    ('MIcrofone', 'Iluminação RGB radiante com efeitos dinâmicos: Personalize a iluminação RGB.', 850.00, 'img8.jpg'),
    ('Mi band', 'Relógio Mi Band 10 (GLOBAL) Inteligente, Tela AMOLED 1,72, Relógio inteligente', 375.00, 'img15.jpg'),
    ('Mouse x11', 'ATTACK SHARK X11 Mouse sem fio leve, 62g, RGB, 22K DPI, sensor PAW3311', 229.00, 'img16.jpg'),
    ('Note', 'V15 ANV15-51-73E9 Intel Core i7-13620H, 16GB RAM, 512GB SSD, NVIDIA RTX 3050', 5119.00, 'img19.jpg'),
    ('Nintendo', 'Bundle Nintendo Switch 2 + Jogo Digital Mario Kart World – Modelo Nacional', 4700.00, 'img23.jpg'),
    ('Rimel Rosa', 'MÁSCARA PARA CÍLIOS PEEL OFF MELU RR515 SELFIE RUBYROS', 20.00, 'melu.jpg'),
    ('Base', 'A base de tratamento da Bauny tem a presença de nonychosine com metionina.', 18.90, 'base-tratamento.jpg'),
    ('Esmalte', 'Quente como um beijo cinematográfico. Quente como um dos nomes queridinhos.', 18.90, 'Theo.jpg'),
    ('Kimono', 'Kimono Karatê adidas Club K220C com selo WKF Utilizado para Kumite.', 349.77, 'kimono.jpg'),
    ('Chuteira', 'Termine o trabalho na Phantom GX 2 Pro. Leve suas habilidades para o próximo nível.', 1139.99, 'chuteira.jpg'),
    ('Meia', 'Treine com a meia de treino com amortecimento Nike Everyday.', 75.99, 'meia.jpg'),
    ('Meia2', 'A Meia NikeCourt Multiplier Cushioned proporciona conforto de nível superior.', 142.49, 'meia2.jpg')
""")

con.commit()
con.close() 

##print("Tabela 'produtos' criada e dados inseridos com sucesso!")
