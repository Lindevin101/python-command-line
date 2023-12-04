from peewee import *

db = PostgresqlDatabase('nbaplayers', user='base2', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Nbaplayer(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    team = CharField()
