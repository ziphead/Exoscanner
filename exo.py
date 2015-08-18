from lxml import etree
from models import *

class Scanner():
    def __init__(self):
        self.dbxml = etree.parse('systems.xml')
        self.tree = self.dbxml.xpath('/systems')
        self.sysid = 1
        self.binid = 1
        self.starid = 1
        self.sysinfo = []   
        self.starinfo = []
        self.bodyinfo = []
        self.bininfo = []
        
    def attr_check(self,attr, text): # this method appends object attributes  in a list
        self.attr = attr
        xlist = []
        for key, val in attr.iteritems():
            val = str(val)
            text = str(text)
            x = text + ' : ' + key + ' = ' + val + ' / '
            xlist.append(x)
        return xlist
        
    def star_finder(self, data, dataid, parent):
        self.starid += 1
        sn = {}   
        if parent == 'binary':
            sn['star'] = self.starid
            sn['parent_binary'] = dataid
        elif parent == 'system': 
            sn['star'] = self.starid
            sn['sys'] = dataid
        for star in data:
            if star.tag == 'planet':
                self.planet_finder(star, self.starid, parent = 'star')
                continue
            if star.tag == 'binary' :
                self.bin_finder(star, self.starid, parent = 'star')
                continue 
            if star.tag == 'name':
                if 'name'  in sn:
                    sn['names'] = sn.get('names', '') + ' ' + star.text
                    continue
                else:
                    sn['name'] = star.text
                    continue
            if star.attrib != '':
                sn[star.tag] = star.text
                attrib = self.attr_check(star.attrib, star.tag) 
                band = ' '.join(attrib)  
                sn['attributes'] = sn.get('attributes', '') + band  
            else :
                sn[star.tag] = star.text
                
        self.starinfo.append(sn)
        
        
    def planet_finder(self, data, dataid, parent):
        bd = {}   
        if parent == 'binary':
            bd['parent_binary'] = dataid
        elif parent == 'star': 
            bd['parent_star'] = dataid
        for planet in data:
            # for planets orbiting other planets : code modifications should be made here (and extra table rows needed)
            if planet.tag == 'name':
                if 'name'  in bd:
                    bd['names'] = bd.get('names', '') + ' ' + planet.text
                    continue
                else:
                    bd['name'] = planet.text
                    continue
            if planet.attrib != '':
                bd[planet.tag] = planet.text
                attrib = self.attr_check(planet.attrib, planet.tag) 
                band = ' '.join(attrib)  
                bd['attributes'] = bd.get('attributes', '') + band  
            else :
                bd[planet.tag] = planet.text
        self.bodyinfo.append(bd)

    def bin_finder(self, data, dataid, parent):
        self.binid += 1
        bn = {}   
        nm = ''
        if parent == 'binary':
            bn['bin'] = self.binid
            bn['parent_binary'] = dataid
        elif parent == 'system': 
            bn['bin'] = self.binid
            bn['sys'] = dataid
        elif parent == 'star':
            bn['bin'] = self.binid 
            bn['star'] = dataid
        for binstar in data:
            if binstar.tag == 'star':
                self.star_finder(binstar, self.binid, parent = 'binary')
                continue
            if binstar.tag == 'planet':
                self.planet_finder(binstar, self.binid, parent = 'binary')
                continue
            if binstar.tag == 'binary' :
                self.bin_finder(binstar, self.binid,  parent = 'binary')
                continue 
            if binstar.tag == 'name':
                if 'name'  in bn:
                    bn['names'] = bn.get('names', '') + ' ' + binstar.text                    
                    continue
                else:
                    bn['name'] = binstar.text
                    continue
            if binstar.attrib != '':
                bn[binstar.tag] = binstar.text
                attrib = self.attr_check(binstar.attrib, binstar.tag) 
                band = ' '.join(attrib)  
                bn['attributes'] = bn.get('attributes', '') + band  
            else :
                bn[binstar.tag] = binstar.text
        self.bininfo.append(bn)


    
    def get_fields(self): # This is the main method  it starts xml iteration, gets 4 lists of unique parameter fields for systems, stars, planets, binaries
        for systems in self.dbxml.xpath('/systems/system'):                       
            self.sysid += 1
            stm = {}
            stm['sys'] = self.sysid
            for system in systems:
                if system.tag == 'star':
                    self.star_finder(system, self.sysid, parent = 'system')
                    continue
                if system.tag == 'planet':
                    self.planet_finder(system, self.sysid, parent = 'system')
                    continue
                if system.tag == 'binary' :
                    self.bin_finder(system, self.sysid,  parent = 'system')
                    continue 
                if system.tag == 'name':
                    if 'name'  in stm:
                        stm['names'] = stm.get('names', '') + ' ' + system.text
                        continue
                    else:
                        stm['name'] = system.text
                        continue
                if system.attrib != '':
                    stm[system.tag] = system.text
                    attrib = self.attr_check(system.attrib, system.tag) 
                    band = ' '.join(attrib)  
                    stm['attributes'] = stm.get('attributes', '') + band  
                else :
                    stm[system.tag] = system.text

            self.sysinfo.append(stm)

        return self.bininfo, self.starinfo, self.bodyinfo, self.sysinfo


if __name__ == "__main__":
    
    x = Scanner().get_fields()    
    try :
        db.connect()
    except:
        handle_exception()
        raise
    
    db.create_tables([System, Binary, Star, Planet],  True)    
    print 'done creating db'

    binlist = sorted(x[0], key=lambda k: k['bin'])
    syslist = sorted(x[3], key=lambda k: k['sys'])
    starlist = sorted(x[1], key=lambda k: k['star'])
    #planlist = sorted(x[2], key=lambda k: k['bin'])
    with db.atomic(): # Bulk insert data
        for data_dict in syslist:
            System.create(**data_dict)
            print data_dict,  '\n system ok'
        for data_dict in binlist:
            Binary.create(**data_dict)
            print data_dict, '\n binary ok'
        for data_dict in starlist:
            Star.create(**data_dict)
            print data_dict, '\n star ok'
        for data_dict in x[2]:
            Planet.create(**data_dict)
            print data_dict, '\n planet ok'

    raw_input('All done. Press any button: ')

