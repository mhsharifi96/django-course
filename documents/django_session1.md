# DJANGO

### step 0 

Q:what is django ? \
answer : 
```
```
[reference](https://www.djangoproject.com/)

-----


Q : What is MVT ? [reference](https://www.geeksforgeeks.org/django-project-mvt-structure/)\
answer : 
```
```

Q : What is difference between MVC and MVT architecture?\
 answer : 
```
```
### step 1
setup environment
```
```
### step 1.1 
installation 

```
    pip install django
    # check which version installed :
    python -m django --version
```

### step 2

create project 
```
django-admin startproject <project_name>
e.x : django-admin startproject maktabSite
```
Let’s look at what startproject created:

```
mysite/
    manage.py  #A command-line utility that lets you interact with this Django project in various ways
    maktabSite/
        __init__.py
        settings.py #Settings/configuration for this Django project
        urls.py #“table of contents” of your Django-powered site.
        asgi.py
        wsgi.py
```

explain about `manage.py`, `asgi.py` , `wsgi.py`.\
answer : 
- **manage.py** : 
-  **asgi.py** : 
-  **wsgi.py** : 


### step 2.1
run server 
```
python manage.py runserver
```
You’ll see the following output on the command line:

```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

September 17, 2022 - 15:50:53
Django version 4.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Congratulations! the server running, check this url` http://127.0.0.1:8000/`

**NOTE :** you can change defualt port form 8000 to any port that you like. e.x : `python manage.py runserver 8888` or `python manage.py runserver 0:8000`
0 is shourtcut for 0.0.0.0.

### step 2.2
run  command : `python manage.py migrate`

Why should we implement this?

### step 3
CREATE APP 
```
python manage.py startapp  blog 
```
That’ll create a directory blog, which is laid out like this:

```
blog/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py

```

what is app ? 

please READ **Fundamentals of Django App Design chapter (4)** on `Two Scoops of Django 3.x book`

---------------

### step 4
create super user \
run command 
```
python manage.py createsuperuser
```

Now, open a Web browser and go to “/admin/” on your local domain,you should see the admin’s login screen

------


### step 5
your sample app(e.x blog), `models.py` file, you can create model like this 


```
from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
```

Q : what are `CASCADE`, `PROTECT`,`RESTRICT`,`SET_NULL`,`SET_DEFAULT`,`SET` in  **on_delete**? (Give an example for each)

answers : 
```
#CASCADE :
    #example
#PROTECT:
    #example
...
```


[refrence](https://docs.djangoproject.com/en/4.1/ref/models/fields/#module-django.db.models.fields.related)

next , you must run below command :
```
python manage.py makemigrations
python manage.py migrate
```
Q : why ?
you should find answer, why command run there

answer : 
```
```

### step 5.1
add model to django admin

in `admin.py`

```
from django.contrib import admin

from . import models

admin.site.register(models.Article)
admin.site.register(models.Reporter)
```


READ : DJANGO FOR BIGGINER book,  chapter 1,2


date : 9/18/2022