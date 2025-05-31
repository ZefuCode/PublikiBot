import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("bot_respuestas.db")
cursor = conn.cursor()

# Crear tablas
cursor.execute('''
CREATE TABLE IF NOT EXISTS respuestas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contenido TEXT NOT NULL,
    menu_id INTEGER,
    FOREIGN KEY (menu_id) REFERENCES menus(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS palabras_clave (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palabra TEXT NOT NULL,
    respuesta_id INTEGER,
    FOREIGN KEY (respuesta_id) REFERENCES respuestas(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS menus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
''')

# Insertar datos de prueba (solo si no hay)
cursor.execute("SELECT COUNT(*) FROM respuestas")
if cursor.fetchone()[0] == 0:
    # Insertar una respuesta (promoción)
    cursor.execute("INSERT INTO respuestas (contenido) VALUES (?)",
                   ("🎁 ¡Has ganado un combo de palomitas gratis!",))
    respuesta_id = cursor.lastrowid

    # Asociar una palabra clave (número de ticket)
    cursor.execute("INSERT INTO palabras_clave (palabra, respuesta_id) VALUES (?, ?)",
                   ("12345678", respuesta_id))

    print("✅ Datos de prueba insertados.")
else:
    print("ℹ️ La base de datos ya contiene datos.")

conn.commit()
conn.close()
