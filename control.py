from models import *
from exo import Scanner
from datetime import datetime

def conn():
    try :
        db.connect()
    except:
        print 'Connection error! Check "models.py" '
        exit()

def update():
    uptime = '2001-01-03'
    x = Scanner().get_fields()   

    for data_dict in x[2]:
        for k,v in data_dict.iteritems():
            if k == 'lastupdate' and v is None:
                continue
            elif k == 'lastupdate':
                lupdate = datetime.strptime(v,'%y/%m/%d').strftime('%Y-%m-%d')
                #print ' something wrong with the date: ' ,v
                #continue
            if lupdate > uptime:
                uptime = lupdate
    print 'looking for ', uptime
    
    try : 
        query = Planet.get(Planet.lastupdate == uptime)
        print query.name , 'is the last found planet. Database is up-to-date.'
    except :
        print 'updating'
        db.drop_tables([Planet, Star, Binary, System ], safe=True,  cascade=True)
        print 'drop old'
        Scanner().create_tables()  
        Scanner().filler(x) 
    raw_input('All done. Press any button: ')
q1 = raw_input('Do you wish to create mysql tables or update? \n  To create tables press (1) To update press (2): ')    
while q1 != '1' or q1 !='2':
    if q1 == '1':
        conn()
        Scanner().create_tables()
        x = Scanner().get_fields() 
        Scanner().filler(x) 
        break
         
    elif q1 == '2':
        print 'trying to update....'  
        conn()  
        update()
        break
         
        
    else: 
        print 'wrong input'
        q1 = raw_input('Do you wish to create mysql tables or update? \n  To create tables press (1) To update press (2): ')    
        

