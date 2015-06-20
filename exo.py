#http://www.openexoplanetcatalogue.com/systems/?filters=habitable
import xml.etree.ElementTree as ET
oec = ET.parse("systems.xml")
class Systems():
    def __init__(self, data):
        self.oec = ET.parse("systems.xml")
<<<<<<< HEAD
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
=======
        self.root = self.oec.getroot()
        self.data = data
    def scan(self):
        self.child = "star"
        self.systemz = self.oec.findall(".//system")
        for system in self.systemz:
            for element in system:
                if element.tag == self.child :
                    element.text = "Something here"
                print element.tag, element.text, self.data, "\n"

x = Systems("huui").scan()
>>>>>>> 6c31697ef84d8fbbc06350b46f8e159af56640a6
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
                
<<<<<<< HEAD
=======
    #print [planet.findtext("name"), planet.findtext("radius")]    
    #if star.findtext("name") == "HD 240210":
        #print star.findtext("name"), "Star type: " , type ,"\n", " mv ", star.findtext("magV"), "\n"
    #else: b = "No type found"
    #print star.findtext("name"), "Srar type: " , star.findtext("magV"), type ,,  
raw_input('hello')
>>>>>>> 6c31697ef84d8fbbc06350b46f8e159af56640a6
