from models import *

for planet in Planet.select():
    if planet.parent_star is not None:
        mommy = ' orbits a star ' + planet.parent_star.name  
    elif  planet.parent_binary is not None:
        if planet.parent_binary.name is not None: # most of binary systems have no name
            mommy = ' orbits binary system ' + str(planet.parent_binary.name) 
        else: mommy = ' orbits binary system without a name ' 
    else: print 'something went wrong here'
    print  'Planet name: ', planet.name, '/ Discovery method: ', planet.discoverymethod,'/',  mommy
