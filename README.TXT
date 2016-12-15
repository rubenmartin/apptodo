git config --global --edit

# After doing this, you may fix the identity used for this commit with:

git commit --amend --reset-author


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

deactivate

brew install nodejs
mkdir todobackend-specs
cd todobackend-specs
git init

name: (todobackend-specs)                                                                    
version: (1.0.0) 0.1.0                                                                       
description: Todobackend Acceptance Tests                                                    
entry point: (index.js) app.js                                                               
test command: mocha                                                                          

npm install bluebird chai chai-as-promised mocha superagent superagent-promise mocha-jenkins-reporter --save


ACCEPTANCE TEST

ACTIVATE AGAIN VENV

python manage.py migrate --settings=todobackend.settings.test
python manage.py runserver --settings=todobackend.settings.test

in specs folder
mocha

cd ..
cd ..

in the root folder before todobackend we create a new app:


git clone https://github.com/rubenmartin/todobackend-client.git
cd todobackend-client
npm install
IN THE TODOBACKEND
ACTIVATE AGAIN 
cd src
python manage.py runserver --settings=todobackend.settings.test

in the client
node app.js

http://localhost:3000

in the browser in the filed todo add: http://localhost:8000/todos
