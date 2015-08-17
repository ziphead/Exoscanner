# Exoscanner

   Exoscanner is a python program, which creates mysql  tables in your database and fills them with data from the Open Exoplanet Catalogue. https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue. It preserves relations between bodies in systems by separating system, star , binary, planet data into 4 tables linked with foreign keys.

Used python modules:
  - lxml
  - peewee



### Version
0.1.0 (Alpha)


### Installation

Tested with Ubuntu 14.4

Before launching this program please make sure you have done the following preparations:
1) Working mysql server on your localhost or on a distant server.
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

6) launch  exo.py

```sh
$ python exo.py

```
7) Check out

```sh
$ python control.py

```

### Development

- Control module (in progress)

**Contacts**

- [Yury Milto]  ymilto@gmail.com