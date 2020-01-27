from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Ad(BaseModel):
    url = CharField(null=False, default='')
    title = CharField(null=False, default='')
