projectName = Tokiyo
-------------------------------------------------------------------------------------------

for creating django project
- install django using "pip install django" in terminal
- "django-admin startproject (projectName)" to generate project
- "python manage.py startapp (projectNameApp)" to generate app
-------------------------------------------------------------------------------------------

add the projectNameApp in settings.py under INSTALLED_APPS
--------------------------------------------------------------------------------------------

config the data in models.py under class
--------------------------------------------------------------------------------------------

-add in admin.py

from .models import *
# Register your models here.
-------------------------------------------------------------------------------------------
- run the below cmd

python manage.py migrate
-------------------------------------------------------------------------------------------

-create super Users

PS C:\Users\admin\Desktop\PYTHON\FirstDjangoProject> python manage.py createsuperuser
Username (leave blank to use 'admin'): purveenram
Email address: purveenram.36@gmail.com
Password:
Password (again):
Superuser created successfully.
--------------------------------------------------------------------------------------------

python manage.py makemigrations TokiyoApp

--------------------------------------------------------------------------------------------

to run server use "python manage.py runserver" in terminal
--------------------------------------------------------------------------------------------

html are stored under folder "templates"
css, js and images are storeed under folder "static"

--------------------------------------------------------------------------------------------
for uploading image pilow has to be install
python -m pip install Pillow

--------------------------------------------------------------------------------------------
form.py & auth_backends.py are craeted for submiting form and backend authentication respectively.

-------------------------------
pip install --upgrade djongo   
pip install --upgrade pymongo  