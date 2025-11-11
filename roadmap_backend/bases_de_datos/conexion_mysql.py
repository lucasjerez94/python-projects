import mysql.connector
from mysql.connector import Error
import sys

print(">>> Debug: Script conexion_mysql.py iniciado correctamente.")
print(f">>> Debug: Python ejecutándose desde: {sys.executable}")
print("🚀 Iniciando script de conexión...")
print("🔍 Intentando conectar a MySQL...")

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin1234!",
        database="prueba_python",
        connection_timeout=5  # fuerza error si no responde
    )

    print("✅ ¡Conexión exitosa!")

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios;")
    resultados = cursor.fetchall()
    print("📦 Datos obtenidos desde MySQL:")
    for fila in resultados:
        print(fila)

except Error as e:
    print(f"❌ Error al conectar o consultar: {e}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("🔒 Conexión cerrada correctamente.")
