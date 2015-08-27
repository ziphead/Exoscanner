# Exoscanner

   Exoscanner is a python program, which creates mysql tables in your database and fills them with data from the Open Exoplanet Catalogue. https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue. It preserves relations between bodies in systems by separating system, star , binary, planet data in 4 tables related with foreign keys.
   Exoscanner is  another instance or a tool to make your own exoplanet SQL database. File "models.py" contains all the tags for each model and you can freely remove some of them or add yours then built your own database with data you need for specific calculations or for a personal web page.
   

![alt tag](http://i58.tinypic.com/flwms.png)

Used python modules:
  - lxml
  - peewee



### Version
0.1.1 (Alpha)

### Issues
-  Spectral type convertation problem


### Installation

Tested with Ubuntu 14.4

Before launching this program please make sure you have done the following preparations:

1) You have mysql server running on your localhost or on a distant server.

2) Exoscanner cooks tables only. You'll need to create a new database or use an existing one. Give mysql user  the priviliges   to insert, delete and  alter table. 

3) Exoscanner is a python 2.7 code. It uses two  libraries which are not icluded in the standart python package. You have to install them manualy with pip.

```sh
$ sudo apt-get install python-pip 
```

```sh
$ pip install peewee
$ pip install lxml

```
4) Download Exoscanner folder then download and extract open exoplanet catalogue (https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz) 

5) Open models.py and type your mysql database name, username and password


6) Check out

```sh
$ python control.py

```

### Development

- Control module (in progress)


**Contacts**

- [Yury Milto]  ymilto@gmail.com
