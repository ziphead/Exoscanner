from lxml import etree

class Systems():
    def __init__(self, data):
        self.dbxml = etree.parse('systems.xml')
        self.tree = self.dbxml.xpath('/systems')
        self.data = data
    def scan(self):
        for system in self.dbxml.xpath('/systems/system'):
            print "=>",system.tag , "system ninfo : ", system.text
            for star in system:
                print "===>",star.tag, "star info : ", star.text
                for planet in star:
                    print "=====>", planet.tag, "planet info : ", planet.text
                    for planetelem in planet:
                        print "========>", planetelem.tag, "planet info : ", planetelem.text

                #print element.tag, element.text, "parent is ",  nm, "\n"

x = Systems("yaayay").scan()
  
raw_input('hello')

