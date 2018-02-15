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

for thing in find_borough("Brooklyn"):
    print thing

for thing in find_zip("11215"):
    print thing

for thing in find_zip_grade('11215', 'A'):
    print thing
#for thing in db:
#   print thing


def find_zip_grade_lt(z,score):
    return collection.find({"$and": [{"address.zipcode":z},{"grades.0.score":{"$lt": score }}]})

for thing in find_zip_grade_lt('11215', 1):
    print thing



def special(borough, score, grade):
    return collection.find({'$and': [{"borough": borough}, {"grades.0.score": score}, {"grades.0.grade": grade}]})

for thing in special("Brooklyn", 6, "A"):
    print thing
                         
 

