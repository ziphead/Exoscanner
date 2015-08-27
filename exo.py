from lxml import etree
import urllib, gzip, io
from models import *

class Scanner():
    def __init__(self):
        url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
        self.dbxml = etree.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.urlopen(url).read())))
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
        
    def separation_check(self, attr, tag): # this method appends object attributes  in a list
        self.attr = attr
        self.tag = tag
        xlist = []
        right_tag = 'separation'
        for key, val in attr.iteritems():
            if val == 'AU':
                right_tag = 'separation_au'
                continue
            elif val == 'arcsec':
                right_tag = 'separation_arcsec'
                continue
            val = str(val)
            tag = str(tag)
            x = tag + ' : ' + key + ' = ' + val + ' / '
            xlist.append(x)
        return right_tag, xlist
    
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
            tag = star.tag.lower()
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
                sn[tag] = star.text
                attrib = self.attr_check(star.attrib, star.tag) 
                band = ' '.join(attrib)  
                sn['attributes'] = sn.get('attributes', '') + band  
            else :
                sn[tag] = star.text
                
        self.starinfo.append(sn)
        
        
    def planet_finder(self, data, dataid, parent):
        bd = {}   
        if parent == 'binary':
            bd['parent_binary'] = dataid
        elif parent == 'star': 
            bd['parent_star'] = dataid
        for planet in data:
            tag = planet.tag.lower()
            # for planets orbiting other planets : code modifications should be made here (and extra table rows needed)
            if planet.tag == 'name':
                if 'name'  in bd:
                    bd['names'] = bd.get('names', '') + ' ' + planet.text
                    continue
                else:
                    bd['name'] = planet.text
                    continue
            if planet.tag == 'separation':
                find_unit = self.separation_check(planet.attrib, planet.tag)
                bd[find_unit[0]] = planet.text                 
                band = ' '.join(find_unit[1])  
                bd['attributes'] = bd.get('attributes', '') + band
                continue
            if planet.attrib != '':
                bd[tag] = planet.text
                attrib = self.attr_check(planet.attrib, planet.tag) 
                band = ' '.join(attrib)  
                bd['attributes'] = bd.get('attributes', '') + band  
            else :
                bd[tag] = planet.text
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
            tag = binstar.tag.lower()            
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
            if binstar.tag == 'separation':
                find_unit = self.separation_check(binstar.attrib, binstar.tag)
                bn[find_unit[0]] = binstar.text                 
                band = ' '.join(find_unit[1])  
                bn['attributes'] = bn.get('attributes', '') + band
                continue
            if binstar.attrib != '':                
                bn[tag] = binstar.text
                attrib = self.attr_check(binstar.attrib, binstar.tag) 
                band = ' '.join(attrib)  
                bn['attributes'] = bn.get('attributes', '') + band  
            else :
                bn[tag] = binstar.text
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

    def create_tables(self):
        db.create_tables([System, Binary, Star, Planet],  True)    
        print 'Creating tables ==> DONE'


    def filler(self, x):
        self.x = x
        binlist = sorted(x[0], key=lambda k: k['bin'])
        syslist = sorted(x[3], key=lambda k: k['sys'])
        starlist = sorted(x[1], key=lambda k: k['star'])
        #planlist = sorted(x[2], key=lambda k: k['bin'])
        with db.atomic(): # Bulk insert data
            for data_dict in syslist:
                System.create(**data_dict)
                #print data_dict,  '\n system ok'
            for data_dict in binlist:
                Binary.create(**data_dict)
                #print data_dict, '\n binary ok'
            for data_dict in starlist:
                Star.create(**data_dict)
                #print data_dict, '\n star ok'
            for data_dict in x[2]:
                Planet.create(**data_dict)
                #print data_dict, '\n planet ok'


if __name__ == "__main__":
    print 'run control.py'
    #Scanner().create_tables()
    #Scanner().filler()


