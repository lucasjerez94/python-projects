def obtener_usuarios(cursor):
    cursor.execute("SELECT id, nombre, correo FROM usuarios")
    return cursor.fetchall()

def insertar_usuario(cursor, nombre, correo):
    cursor.execute(
        "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)",
        (nombre, correo)
    )

import pymysql

conexion = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="Admin1234!",
    database="prueba_python",
    port=3306
)

cursor = conexion.cursor()

insertar_usuario(cursor, "Juan", "juan@email.com")
conexion.commit()

usuarios = obtener_usuarios(cursor)

print("📋 Usuarios:")
for u in usuarios:
    print(u)

cursor.close()
conexion.close()
