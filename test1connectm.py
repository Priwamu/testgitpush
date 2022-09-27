import pymongo
client = pymongo.MongoClient("mongodb+srv://wanjiruwandi:wandi_1979@shiru.clqdskk.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data1 = {"name":"wairimu",
         "mail_id" : "wairimu@abc.ai",
         "subjects" : ["data_science","big data","data analytics"]

}
list_of_records = [
    {'companyName': 'patika',
     'product': 'Affordable AI',
     'courseoffered': 'Deep learning for NLP and computer vision'},

    {'companyName': 'patika',
     'product': 'Affordable AI',
     'courseoffered': 'Deep learning for NLP and computer vision'},

    {'companyName': 'patika',
     'product': 'Affordable AI',
     'courseoffered': 'Deep learning for NLP and computer vision'}
]

# collection is like a table ,document is the dta
database = client['myinfo']
collection = database["pat"]
#collection.insert_one(data1)
collection.insert_many(list_of_records)

collection1 = database['samplejson']
data2 = {
  "users": [
    {
      "userId": 1,
      "firstName": "Krish",
      "lastName": "Lee",
      "phoneNumber": "123456",
      "emailAddress": "krish.lee@learningcontainer.com"
    },
    {
      "userId": 2,
      "firstName": "racks",
      "lastName": "jacson",
      "phoneNumber": "123456",
      "emailAddress": "racks.jacson@learningcontainer.com"
    },
    {
      "userId": 3,
      "firstName": "denial",
      "lastName": "roast",
      "phoneNumber": "33333333",
      "emailAddress": "denial.roast@learningcontainer.com"
    },
    {
      "userId": 4,
      "firstName": "devid",
      "lastName": "neo",
      "phoneNumber": "222222222",
      "emailAddress": "devid.neo@learningcontainer.com"
    },
    {
      "userId": 5,
      "firstName": "jone",
      "lastName": "mac",
      "phoneNumber": "111111111",
      "emailAddress": "jone.mac@learningcontainer.com"
    }
  ]
}
collection1.insert_one(data2)
record = collection.find()
for i in record:
    print(i)
# extract dta from mongodb

#data3 = collection.find({"companyname": "patika"})
data3 = collection.find({"courseoffered":{"$gt" : "E"}})
for i in data3:
    print(i)


