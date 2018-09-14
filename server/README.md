### Comments

-  Install python3
-  Install pip3
-  Create virtual environment
```
sudo apt install virtualenv
```
-  Activate virtualenv
```
virtualenv env
source env/bin/activate
```
-  Install django & djangorestframework + dependencies
```
pip3 install django
pip3 install djangorestframework
pip3 install psycopg2
```
-  Install MQTT for Python
```
pip3 install paho-mqtt
```
-  Install PSQL locally
```
sudo apt install postgresql
```
-  Start Docker Postgres container on port 25432
-  Ensure crendentials match to connect to server
```
CREATE USER petprototype WITH password '123123';
CREATE DATABASE petprototype;
```

-  Migrate
```
python3 manage.py migrate
```
-  Run server
```
python3 manage.py runserver
```
