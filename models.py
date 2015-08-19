from peewee import *
db = MySQLDatabase('your_db_name', user='msql_user',passwd='password') # Type your mysql parameters here


class BaseModel(Model):
    class Meta:
        database = db

class System(BaseModel):
    attributes = TextField(null=True)
    declination = CharField(null=True)
    distance = FloatField(null=True)
    epoch = CharField(null=True)
    names = TextField(null=True)
    rightascension = CharField(null=True)
    sys = IntegerField(db_column='sys_id', primary_key=True) # Don't change this line
    name = CharField(null=True)
    videolink = CharField(null=True)

    class Meta:
        db_table = 'System'

class Binary(BaseModel):
    ascendingnode = FloatField(null=True)
    attributes = TextField(null=True)
    bin = IntegerField(db_column='bin_id', primary_key=True) # Don't change this line
    name = CharField(null=True)
    names = TextField(null=True)
    eccentricity = FloatField(null=True)
    inclination = FloatField(null=True)
    longitude = FloatField(null=True)
    magb = FloatField(db_column='magB', null=True)
    magh = FloatField(db_column='magH', null=True)
    magi = FloatField(db_column='magI', null=True)
    magj = FloatField(db_column='magJ', null=True)
    magk = FloatField(db_column='magK', null=True)
    magr = FloatField(db_column='magR', null=True)
    magv = FloatField(db_column='magV', null=True)
    meananomaly = FloatField(null=True)
    parent_binary = ForeignKeyField(db_column='parent_binary', null=True, rel_model='self', to_field='bin') # Don't change this line
    periastron = FloatField(null=True)
    periastrontime = FloatField(null=True)
    period = FloatField(null=True)
    positionangle = FloatField(null=True)
    semimajoraxis = FloatField(null=True)
    separation = FloatField(null=True)
    sys = ForeignKeyField(db_column='sys_id', null=True, rel_model=System, to_field='sys') # Don't change this line
    transittime = FloatField(null=True)

    class Meta:
        db_table = 'Binary'

class Star(BaseModel):
    age = FloatField(null=True)
    attributes = TextField(null=True)
    parent_binary = ForeignKeyField(db_column='bin_id', null=True, rel_model=Binary, to_field='bin') # Don't change this line
    magb = FloatField(db_column='magB', null=True)
    magh = FloatField(db_column='magH', null=True)
    magi = FloatField(db_column='magI', null=True)
    magj = FloatField(db_column='magJ', null=True)
    magk = FloatField(db_column='magK', null=True)
    magr = FloatField(db_column='magR', null=True)
    magv = FloatField(db_column='magV', null=True)
    mass = FloatField(null=True)
    metallicity = FloatField(null=True)    
    radius = FloatField(null=True)
    spectraltype = CharField(null=True)
    star = IntegerField(db_column='star_id', primary_key=True) # Don't change this line
    name = CharField(null=True)
    names = TextField(null=True)
    sys = ForeignKeyField(db_column='sys_id', null=True, rel_model=System, to_field='sys') # Don't change this line
    temperature = FloatField(null=True)

    class Meta:
        db_table = 'Star'

class Planet(BaseModel):
    age = FloatField(null=True)
    ascendingnode = FloatField(null=True)
    attributes = TextField(null=True) 
    parent_binary = ForeignKeyField(db_column='bin_id', null=True, rel_model=Binary, to_field='bin') # Don't change this line
    description = TextField(null=True)
    discoverymethod = CharField(null=True)
    discoveryyear = IntegerField(null=True)  # year
    eccentricity = FloatField(null=True)
    inclination = FloatField(null=True)
    istransiting = IntegerField(null=True)
    lastupdate = DateField(null=True)
    longitude = FloatField(null=True)
    magb = FloatField(db_column='magB', null=True)
    magh = FloatField(db_column='magH', null=True)
    magi = FloatField(db_column='magI', null=True)
    magj = FloatField(db_column='magJ', null=True)
    magk = FloatField(db_column='magK', null=True)
    magr = FloatField(db_column='magR', null=True)
    magv = FloatField(db_column='magV', null=True)
    mass = FloatField(null=True)
    meananomaly = FloatField(null=True)
    periastron = FloatField(null=True)
    periastrontime = FloatField(null=True)
    period = FloatField(null=True)
    name = CharField(null=True)
    names = TextField(null=True)
    positionangle = FloatField(null=True)
    radius = FloatField(null=True)
    semimajoraxis = FloatField(null=True)
    separation = FloatField(null=True)
    spectraltype = CharField(null=True)
    spinorbitalignment = FloatField(null=True)
    parent_star = ForeignKeyField(db_column='star_id', null=True, rel_model=Star, to_field='star') # Don't change this line
    temperature = FloatField(null=True)
    transittime = FloatField(null=True)

    class Meta:
        db_table = 'Planet'
