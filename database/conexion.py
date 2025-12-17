import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin1234!",
        database="prueba_python",
        port=3306
    )

    if conexion.is_connected():
        print("✅ Conexión exitosa a MySQL")
        print("Servidor:", conexion.get_server_info())

except Error as e:
    print("❌ Error al conectar a MySQL:", e)

finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("🔒 Conexión cerrada")
