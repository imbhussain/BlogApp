# BlogApp
Blog Application using Django 
## Installation Guide:
* Prerequisite for Django is python installation on your operating system. Latest version of python can be downloaded from https://www.python.org/downloads/  python brings packages/libraries used by Django and your other Python apps. 
* After installation python version can be checked by opening command prompt and executing **python –version**. If you are using a python version older than 3.4, then you need to install PIP which is a package manager for python. Open a command prompt and execute **easy_install pip**. Pip will be installed to your system. 
* Now you can install Django using pip. Open the command prompt and execute **pip install django**. This will automatically download and install Django. Installation can be verified by executing **django-admin –version**. 
* Now Django project can be created just get a terminal and navigate where you want your project folder and execute **django-admin startproject yourprojectname**.
* After project creation and necessary configurations, you can run your project by executing **python manage.py runserver**.


## Project Guide:
This project is a simple blogging web application, where blogs can be posted and user can access the information as well as can perform some other tasks by visiting the following URLs:
* Home page can be accessed by visiting http://127.0.0.1:8000/ 
* New Blogs can be posted via http://127.0.0.1:8000/blogpost/ 
* User can Login by visiting http://127.0.0.1:8000/login/ this page. User can update and delete the posts after logging in. Credentials to login: Username “**testuser**” and password “**internship**”.
* 	Only admin can login to database. Admin page can be accessed by visiting http://127.0.0.1:8000/admin/login/?next=/admin/ this page. Credentials for admin are username “**admin**” and password “**bosch123**”. Admin can add, delete and update the users, admin can also provide the access of updating and deleting the posts to user.
* 	About page can be accessed by visiting this URL http://127.0.0.1:8000/about/ 
*	User can access contact page via http://127.0.0.1:8000/contact/ and after filling the form users can submit their query. 
 
