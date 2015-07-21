from lxml import etree
from peewee import *
db = MySQLDatabase('exop', user='root',passwd='123')
class Catmodel(Model):
    class Meta:
        database = db
class Scanner():
    def __init__(self):
        self.dbxml = etree.parse('systems.xml')
        self.tree = self.dbxml.xpath('/systems')
        self.sysinfo = []   
        self.starinfo = []
        self.bodyinfo = []    
    
    def get_fields(self): # This method gets 3 lists of unique parameter fields for systems, stars, planets
        for system in self.dbxml.xpath('/systems/system'):                       
            for star in system:
                for sun in star:
                    for body in sun:
                        if body.tag not in self.bodyinfo :              
                            self.bodyinfo.append(body.tag)
                        else: continue
                    if sun.tag not in self.starinfo :              
                        self.starinfo.append(sun.tag)
                    else: continue 
                if star.tag not in self.sysinfo :              
                    self.sysinfo.append(star.tag)
                else: continue
        return self.sysinfo, self.starinfo, self.bodyinfo
 

x =   Scanner().get_fields()    

for i in x:
    print i
sysattrs = {field: CharField() for field in x[0]}
starattrs = {field: CharField() for field in x[1]}
bodyattrs = {field: CharField() for field in x[2]}
Systems = type('Systems', (Catmodel,), sysattrs)
Stars = type('Stars', (Catmodel,), starattrs)
Bodies = type('Bodies', (Catmodel,), bodyattrs)


db.connect()

db.create_tables([Systems, Stars, Bodies], safe=True)

  
raw_input('hello')

