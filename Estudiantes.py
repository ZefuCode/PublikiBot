import sqlite3
import re

# Crear/conectar la base de datos
conn = sqlite3.connect("estudiantes.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    correo TEXT NOT NULL
)
''')
conn.commit()

# Validar correo electrónico
def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

# Agregar estudiante
def agregar_estudiante():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    correo = input("Correo: ")
    if not validar_correo(correo):
        print("Correo no válido. Intenta de nuevo.")
        return
    cursor.execute("INSERT INTO estudiantes (nombre, edad, correo) VALUES (?, ?, ?)", (nombre, edad, correo))
    conn.commit()
    print("Estudiante agregado correctamente.")

# Mostrar todos los estudiantes
def mostrar_estudiantes():
    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()
    print("\nEstudiantes registrados:")
    for est in estudiantes:
        print(f"ID: {est[0]}, Nombre: {est[1]}, Edad: {est[2]}, Correo: {est[3]}")

# Buscar estudiante por nombre
def buscar_estudiante():
    nombre = input("Ingrese el nombre a buscar: ")
    cursor.execute("SELECT * FROM estudiantes WHERE nombre LIKE ?", ('%' + nombre + '%',))
    resultados = cursor.fetchall()
    if resultados:
        for est in resultados:
            print(f"ID: {est[0]}, Nombre: {est[1]}, Edad: {est[2]}, Correo: {est[3]}")
    else:
        print("No se encontraron coincidencias.")

# Menú
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante por nombre")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            buscar_estudiante()
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

# Ejecutar menú
menu()

# Cerrar conexión
conn.close()