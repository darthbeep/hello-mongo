from pymongo import MongoClient
import json

c = MongoClient("lisa.stuy.edu",27017)
db = c.lastMinute
collection = db.astroids

if collection.count() == 0:
    met = open("astroid.json", "r")
    s = met.read()
    met.close()   
    collection.insert_many(json.loads(s))
else:
    print "Already imported"

def find_orbit_class(name):
    return collection.find({'orbit_class':name})

def smaller_period_year(year):
    return collection.find({"period_yr":{"$lt": year }})


def find_h_mag(value):
    return collection.find({"h_mag":value})


def special(name, year, value):
    return collection.find({'$and': [{"orbit_class": name}, {"period_yr": year}, {"h_mag": value}]})

for thing in find_orbit_class("Apollo"):
    print thing
    print "Printed all values in this orbit class."

for thing in smaller_period_year("5"):
   print thing
   print "Printed all period years smaller than value"

    
for thing in find_h_mag("21.2"):
    print thing
    print "Printed all h_mag with this value."

for thing in special("Apollo", "1.39", "20.9"):
    print thing
    print "Printed specific astroid"
