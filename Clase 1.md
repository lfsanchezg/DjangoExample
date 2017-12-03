# Clase 1
En Ubuntu

````
sudo apt-get install python3.6
sudo apt-get install python-pip3.6
sudo pip3 install virtualenvwrapper

# instalar los scripts en el .bashrc

workon # muestra los virtual envs del computador
mkvirtualenv --python=/usr/bin/python3 example
python --version
````


````
# scripts a pegar en bashrc

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
````

````
workon <nombre>
pip install django=1.11.6
django-admin startproject <nombre>
cd <nombre>
./manage.py startapp <nombre app>
./manage.py runserver  
````
