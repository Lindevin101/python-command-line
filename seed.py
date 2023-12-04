
from peewee import *
from main import Nbaplayer
from main import db
import json

db.connect()
db.drop_tables([Nbaplayer])
db.create_tables([Nbaplayer])

file = open('nbaplayers.json')
data = json.load(file)

Nbaplayer.insert_many(data).execute()