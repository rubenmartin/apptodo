
pip install virtualenvwrapper-win
.\venv\Scripts\activate.bat

pip install pip --upgrade
pip install django
pip install djangorestframework
pip install django-cors-headers
# Generate the data
python manage.py migrate

# to run the application
python manage.py runserver

# DB install mysql
brew install homebrew/versions/mysql56
mysql.server start
mysql -u root -p

create database todobackend;
grant all privileges on *.* to 'todo'@'localhost' identified by 'password';

pip install mysql-python

python manage.py test --settings=todobackend.settings.test

pip install django-nose

pip install pinocchio

pip install coverage

python manage.py test --settings=todobackend.settings.test

