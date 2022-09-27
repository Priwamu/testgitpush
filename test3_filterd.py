import pymongo

data = [
    {
        "item": "canvas",
        "qty": 100,
        "size": {"h": 28, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "journal",
        "qty": 25,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mat",
        "qty": 85,
        "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mousepad",
        "qty": 25,
        "size": {"h": 19, "w": 22.85, "uom": "cm"},
        "status": "P",
    },
    {
        "item": "notebook",
        "qty": 50,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "P",
    },
    {
        "item": "paper",
        "qty": 100,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "D",
    },
    {
        "item": "planner",
        "qty": 75,
        "size": {"h": 22.85, "w": 30, "uom": "cm"},
        "status": "D",
    },
    {
        "item": "postcard",
        "qty": 45,
        "size": {"h": 10, "w": 15.25, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketchbook",
        "qty": 80,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketch pad",
        "qty": 95,
        "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
        "status": "A",
    },
]

client = pymongo.MongoClient(
    "mongodb+srv://wanjiruwandi:wandi_19879@shiru.clqdskk.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['inventory']
collection = database["stock"]
 collection.insert_many(data)
# FILTER OPERATION
d = collection.find({'status':'A'})
 for i in d:
   print(i)

# condition where status is either A OR P
 d = collection.find({'status': {'$in': ['A', 'P']}})
 for i in d:
   print(i)

# condition where status should b greater than C
 d = collection.find({'status': {'$gt': 'C'}})
for i in d:
   print(i)

# condition where quantity is = 100

 d = collection.find({'qty': 100})
 for i in d:
   print(i)

# condition where quantity is greater than  or = 75

 d = collection.find({'qty': {'$gte': 75}})
 for i in d:
   print(i)

# condition where  item  is sketch pad & qty=95
 d = collection.find({'item': 'sketch pad', 'qty': 95})
 for i in d:
 print(i)

# condition where item is sketch pad and qty is >= 75

 d = collection.find({'item': 'sketch pad', 'qty': {'$gte': 75}})
for i in d:
   print(i)


#   condition where either or OR is satisfied- 2 conditions either way

 d = collection.find({'$or': [{'item': 'sketch pad'}, {'qty': {'$gte': 75}}]})
 for i in d:
    print(i)

# update some records.change values

 collection.update_one({'item': 'canvas'}, {'$set': {'item': 'sudth'}})
 d = collection.find({'item': 'sudth'})
 for i in d:
    print(i)

# delete condition

collection.delete_one({'item': 'sudth'})
