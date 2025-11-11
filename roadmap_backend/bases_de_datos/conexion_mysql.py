import mysql.connector
from mysql.connector import Error

print("🚀 Iniciando script de conexión...")

try:
    print("🔍 Intentando conectar a MySQL...")
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin1234!",
        database="prueba_python"
    )

    print("📡 Estado de la conexión:", conexion.is_connected())

    if conexion.is_connected():
        print("✅ Conexión exitosa a la base de datos MySQL.")
        print("Versión del servidor:", conexion.get_server_info())
    else:
        print("⚠️ No se pudo establecer la conexión.")

except Error as e:
    print("❌ Error al conectar a MySQL:", e)

finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("🔒 Conexión cerrada.")
