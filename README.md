# django-portfolio
Multi webpage with profile,project,login system in django

Dependency
Django-```pip install django```
Django is a high-level Python Web framework

To Run this Project use the following command


1.```python -m venv env```
creates virtual enviroment

2.```python manage.py makemigrations```
generates the SQL commands for preinstalled app

3.```python manage.py migrate```
migrate executes those SQL commands in the database file

3.```Python manage.py migrate --run-syncdb```
reconstruct database schema according to altered model fields(not necessary)

4.```python manage.py createsuperuser```
It will create an admin superuser with all Administrative privileges

5.```python manage.py runserver```
runs the server on localhost.
127.0.0.1:8000

Home page
![Home Page](./output/output1.png)


Project page
![Project Page](./output/output2.png)


Contact page
![Contact Page](./output/output3.png)


Login page
![Login Page](./output/output4.png)