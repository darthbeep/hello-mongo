'''
Information:
Dataset: https://data.nasa.gov/resource/2vr3-k9wn.json
Information about Near-Earth Asteroids and Comets, which I may have accidently misspelled in several places.
We imported it by reading a json file and turning it into a dict and then sending it. We sent them all with insert many after importing them all. Probably not that different from every other team. The perl version is way cooler.
'''


from pymongo import MongoClient
import json

#connect
c = MongoClient("homer.stuy.edu",27017)
db = c.lastMinute
collection = db.astroids

#import data
if collection.count() == 0:
    met = open("astroid.json", "r")
    s = met.read()
    met.close()
    collection.insert_many(json.loads(s))
else:
    print "Already imported"

#gets all the data you can get about astroids
def find_name(name):
    return collection.find({'name':name})

def smaller_reclat(year):
    return collection.find({"reclat":{"$lt": year }})


def find_fall(value):
    return collection.find({"fall":value})


def special(name, year, value):
    return collection.find({'$and': [{"name": name}, {"nametype": year}, {"recclass": value}]})

#and test
for thing in find_name("Aachen"):
    print thing
'''
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
'''
