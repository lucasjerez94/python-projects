from pymongo import MongoClient

# 1. Conectarse a MongoDB local
client = MongoClient("mongodb://localhost:27017")

# 2. Acceder a la base de datos (se crea sola)
db = client["prueba_mongo"]

# 3. Acceder a la colección (se crea sola)
usuarios = db["usuarios"]

# 4. Insertar un documento
resultado = usuarios.insert_one({
    "nombre": "Lucas",
    "perfil": "Analista de Sistemas",
    "stack": ["Python", "React", "MongoDB"],
    "activo": True
})

print("Documento insertado con ID:", resultado.inserted_id)

"""
print("Usuarios en la colección:\n")

for usuario in usuarios.find():
    print(usuario)
"""