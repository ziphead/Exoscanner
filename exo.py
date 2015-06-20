#http://www.openexoplanetcatalogue.com/systems/?filters=habitable
import xml.etree.ElementTree as ET
oec = ET.parse("systems.xml")
class Systems():
    def __init__(self, data):
        self.oec = ET.parse("systems.xml")
        #self.root = self.oec.find("..")
        self.data = data
    def scan(self):
        self.child = "star"
        self.systemz = self.oec.findall(".//system*")
        for system in self.systemz:
            sysnm = system.find("./name").text
            print "system name => ", sysnm
            for star in system:
                starnm = star.find("./name").text
                print "star name ==> ", starnm
                for planet in star:
                    planm = planet.find("./name").text
                    print "planet name ===> ", starnm
               #print element.tag, element.text, "parent is ",  nm, "\n"

x = Systems("yaayay").scan()
print  "====>", x
        
#systems = oec.findall(".//system")
#stars = oec.findall(".//star")
#planets = oec.findall(".//planets")
#for star in stars :
   # print "Star info", star.find("..//name").text
   # for lb in star :
        
    #    if lb.tag == "spectraltype" or lb.tag == "name":     
   #          try :
    #             lb.text.decode('utf8')
     #        except UnicodeEncodeError:
    #             lb.text = "cannot decode to utf"
     #   print "==>", lb.tag,"====>", lb.text,  "\n"
                
