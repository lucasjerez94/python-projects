from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.son import SON

client = MongoClient("127.0.0.1", 27019)

db = client.neuraldb

people = db.people

people.insert_one({"name": "Mike", "age": 30})

#probar
# mike_id =people.insert_one({"name": "Mike", "age": 30}) .inserted_id

people.insert_one({"name": "Lisa", "age": 20, "interests": ["C++", "Python", "Piano"]}) 
people.insert_one({"name": "Mike", "age": 40}) 
people.insert_one({"name": "Mike", "age": 27}) 
people.insert_one({"name": "Lisa", "age": 26, "interests": ["C++", "Python", "Piano"]}) 
people.insert_one({"name": "John", "age": 78}) 



for person in people.find():
      print(person)

#print(mike_id)

#print([p for p in people.find({"_id": ObjectId("valorid")})])

#print([p for p in people.find({"age": {"$lt": 25}})])

#print(people.count_documents({"name": "Lisa"}))

# people.update_oone({"_id": ObjectId("valorid")}, {"$set": {"age": 27}})

#people.delete_many({"age": {"$lt": 25}})

pipeline = [
      {
            "$group": {
                  "_id": "$name",
                  "averageAge": {"$avg": "$age"}
            }
      },
      {
            "$sort": SON([("averageAge", -1), ("_id", -1)])
      }
]

results = people.aggregate(pipeline)

for result in results:
      print(result)
