from models import *

for person in Planet.select():
    if person.parent_star is not None:
        mommy = ' orbits a star ' + person.parent_star.name  
    elif  person.parent_binary is not None:
        if person.parent_binary.name is not None: # most of binary systems have no name
            mommy = ' orbits binary system ' + str(person.parent_binary.name) 
        else: mommy = ' orbits binary system without a name ' 
    else: print 'something went wrong here'
    print  'Planet name: ', person.name, '/ Discovery method: ', person.discoverymethod,'/',  mommy
