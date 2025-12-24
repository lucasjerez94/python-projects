from pymongo import MongoClient
from bson.son import SON

# 1 Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017")

# 2 Base de datos y colección
db = client.neuraldb
people = db.people

# (opcional) Limpiamos la colección para no duplicar datos
people.delete_many({})

# 3 Insertar documentos (datos "crudos")
people.insert_many([
    {"name": "Mike", "age": 30},
    {"name": "Lisa", "age": 20, "interests": ["C++", "Python", "Piano"]},
    {"name": "Mike", "age": 40},
    {"name": "Mike", "age": 27},
    {"name": "Lisa", "age": 26, "interests": ["C++", "Python", "Piano"]},
    {"name": "John", "age": 78}
])

print("📌 Documentos insertados:\n")

# 4 Leer documentos tal cual estan
for person in people.find():
    print(person)

# 5 Pipeline de agregación
pipeline = [
    {
        "$group": {
            "_id": "$name",                 # agrupar por nombre
            "averageAge": {"$avg": "$age"}  # calcular promedio de edad
        }
    },
    {
        "$sort": SON([("averageAge", -1)]) # ordenar por promedio descendente
    }
]

print("\n📊 Resultado del pipeline:\n")

# 6 EJECUTAR PIPELINE
for result in people.aggregate(pipeline):
    print(result)