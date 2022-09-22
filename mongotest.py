import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://wanjiruwandi:wandi_1979@shiru.clqdskk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "wakiru",
    "email": "wakiru@iat.ai",
    "surname": "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
