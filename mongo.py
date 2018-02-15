import pymongo

from pymongo import MongoClient
client = MongoClient('homer.stuy.edu')
db = client.test
collection = db.restaurants
#print collection

def find_borough(b):
    return collection.find({'borough':b})

def find_zip(z):
    return collection.find({'address':{'zipcode':z}})

for thing in find_zip('11218'):
    print thing
#for thing in db:
#    print thing
