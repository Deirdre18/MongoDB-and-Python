import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "mydbtest1"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        #conn = pymongo.MongoClient(url)
        
        conn = pymongo.MongoClient("mongodb://root:trickORTREAT2019@ds163162.mlab.com:63162/mydbtest1")
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

#BASICS OF CRUD COMMANDS FROM PYTHON FILE.

#inserting new record by creating dictionary with key:value pairs and assigning to our variable 'new_doc'.
#new_doc = {'first':'douglas', 'last':'adams', 'dob':'11/03/1952', 'hair_colour': 'grey', 'occupation':'writer', 'nationality':'english'}

#inserting into collection.
#coll.insert(new_doc)

#if adding more than one record, we create an array. 
#new_docs = [{'first':'terry', 'last':'prachett', 'dob':'18/04/1948', 'gender':'m', 'hair_colour': 'not much', 'occupation':'writer', 'nationality':'english'}, {'first':'george', 'last':'rr martin', 'dob':'20/09/1948', 'hair_colour': 'white', 'occupation':'writer', 'nationality':'american'}]

#using insert_many() method
#coll.insert_many(new_docs)

#keeping find function to iterate through and print to screen, and see the new record inserted.
#documents = coll.find()

#documents = coll.find({'first': 'douglas'})

#taking off 'documents =' in front. Deleting data.
coll.remove({'first': 'douglas'})

#updating using search string and creating pair:value dictionary ()
#coll.update_one({'nationality':'american'}, {'$set': {'hair_color':'maroon'}})
coll.update_many({'nationality':'american'}, {'$set': {'hair_color':'maroon'}})

#filter our search with find method() and send in dictionary with nationality of american.

#documents = coll.find()
#filter our search with find method() and send in dictionary with nationality of american.
documents = coll.find({'nationality':'american'})

for doc in documents:
    print(doc)