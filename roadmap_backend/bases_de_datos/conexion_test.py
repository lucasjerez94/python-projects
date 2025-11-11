import mysql.connector

print("Conectando...")

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin1234!",
    database="prueba_python"
)

print("Conectado!")

conexion.close()
print("Conexión cerrada.")
