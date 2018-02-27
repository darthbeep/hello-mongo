import json
from pymongo import MongoClient
c = MongoClient("homer.stuy.edu",27017)
db = c.lastMinute
collection = db.astroids


def read_text():
    f = open('util/astroid.json')
    use = f.read()
    f.close()
    return use#.decode('unicode_escape').encode('ascii','ignore').replace("&#34;", "\n") #Credit to stackoverflow for this one

def string_to_mongo():
    collection.drop()
    string = read_text()
    mongo = json.loads(string)
    collection.insert_many(mongo)

def find(lookingfor):
    return collection.find(lookingfor);

def findall():
    return collection.find()
