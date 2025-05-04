import sqlite3

# Conexión y creación de base de datos
conn = sqlite3.connect("bot_respuestas.db")
cursor = conn.cursor()

# Tabla de respuestas
cursor.execute('''
CREATE TABLE IF NOT EXISTS respuestas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contenido TEXT NOT NULL,
    menu_id INTEGER,
    FOREIGN KEY (menu_id) REFERENCES menus(id)
)
''')

# Tabla de palabras clave
cursor.execute('''
CREATE TABLE IF NOT EXISTS palabras_clave (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palabra TEXT NOT NULL,
    respuesta_id INTEGER,
    FOREIGN KEY (respuesta_id) REFERENCES respuestas(id)
)
''')

# Tabla de menús
cursor.execute('''
CREATE TABLE IF NOT EXISTS menus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
''')

conn.commit()
print("Base de datos creada exitosamente.")
conn.close()
