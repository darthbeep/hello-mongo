import pymongo

from pymongo import MongoClient
client = MongoClient('homer.stuy.edu')
db = client.test
collection = db.restaurants
#print collection

def find_borough(b):
    return collection.find({'borough':b})

def find_zip(z):
    return collection.find({'address.zipcode':z})

def find_zip_grade(z, g):
    return collection.find({'address.zipcode':z, 'grades.0.grade':g})

for thing in find_zip_grade('11215', 'A'):
    print thing
#for thing in db:
#    print thing
