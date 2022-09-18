# DJANGO - SESSION 2

### step 1
run `python manage.py shell `
[reference](https://docs.djangoproject.com/en/4.1/ref/django-admin/#shell)
```
# Import the models we created from our "blog" app
>>> from blog.models import Article, Reporter

# No reporters are in the system yet.
>>> Reporter.objects.all()
<QuerySet []>

# Create a new Reporter.
>>> r = Reporter(full_name='John Smith')

# Save the object into the database. You have to call save() explicitly.
>>> r.save()

# Now it has an ID.
>>> r.id
1

# Now the new reporter is in the database.
>>> Reporter.objects.all()
<QuerySet [<Reporter: John Smith>]>

# Fields are represented as attributes on the Python object.
>>> r.full_name
'John Smith'

# Django provides a rich database lookup API.
>>> Reporter.objects.get(id=1)
<Reporter: John Smith>
>>> Reporter.objects.get(full_name__startswith='John')
<Reporter: John Smith>
>>> Reporter.objects.get(full_name__contains='mith')
<Reporter: John Smith>
>>> Reporter.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Reporter matching query does not exist.

# Create an article.
>>> from datetime import date
>>> a = Article(pub_date=date.today(), headline='Django is cool',
...     content='Yeah.', reporter=r)
>>> a.save()

# Now the article is in the database.
>>> Article.objects.all()
<QuerySet [<Article: Django is cool>]>

# Article objects get API access to related Reporter objects.
>>> r = a.reporter
>>> r.full_name
'John Smith'

# And vice versa: Reporter objects get API access to Article objects.
>>> r.article_set.all()
<QuerySet [<Article: Django is cool>]>

# The API follows relationships as far as you need, performing efficient
# JOINs for you behind the scenes.
# This finds all articles by a reporter whose name starts with "John".
>>> Article.objects.filter(reporter__full_name__startswith='John')
<QuerySet [<Article: Django is cool>]>

# Change an object by altering its attributes and calling save().
>>> r.full_name = 'Billy Goat'
>>> r.save()

# Delete an object with delete().
>>> r.delete()
```


### step 2 :
## CRUD 

### step 2.1 :
create and save  new instance : [reference ](https://docs.djangoproject.com/en/4.1/topics/db/queries/#creating-objects)
```
```

### step 2.2 :
Read instance : [reference](https://docs.djangoproject.com/en/4.1/topics/db/queries/#retrieving-objects)
```
```

### step 2.3 :

update instance :

```
```

### step 2.4
delete instance [reference](https://docs.djangoproject.com/en/4.1/topics/db/queries/#deleting-objects)
```
```

### step 3
[Field options](https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-options)

- null
- blank
- choices
- db_column
- db_index
- default
- editable
- primary_key
- unique
- validators

Q:what is difference between `blank` and `null` ?\
answer : 
```
```


### step 4
[model field type](https://docs.djangoproject.com/en/4.1/topics/db/queries/#deleting-objects)

- AutoField
- BooleanField
- CharField
-  TextField # for large string
-  DateField
-  DateTimeField
-  DecimalField
-  EmailField
-  FileField
-  FloatField
-  ImageField
-  IntegerField
-  JSONField
-  SlugField
-  [Relationship fields](https://docs.djangoproject.com/en/4.1/ref/models/fields/#module-django.db.models.fields.related)
   -  ForeignKey
   -  ManyToManyField
   -  OneToOneField

Q:what is difference between `CharField` and `TextField` ?\
answer : 
```
```
Q:what is difference between `DateField` and `DateTimeField` ?\
answer : 
```
```
Q:what is `SlugField`?\
answer : 
```
```

### step 5
making query

first add  model to  your project (e.x : blog/models.py)
```
from datetime import date

from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
```
Next, run `migrate` and `makemigrations` command. and follow this [link](https://docs.djangoproject.com/en/4.1/topics/db/queries/).

important notes that you should learn in this document.
* Create and saving new instance.
* deleteing instance.
* Retrieving objects
  * Retrieving all objects with all().
  * Retrieving specific objects with filters().
  * Retrieving a single object with get().
  * Limiting QuerySets.
  * Field lookups (WHERE clause)
    * lte/lt
    * gte/gt
    * exact/iexact
    * (i)startswith, (i)endswith
    * (i)contains
    * [Lookups that span relationships](https://docs.djangoproject.com/en/4.1/topics/db/queries/#lookups-that-span-relationships)
* [Many-to-many relationships](https://docs.djangoproject.com/en/4.1/topics/db/queries/#many-to-many-relationships)
* [One-to-one relationships](https://docs.djangoproject.com/en/4.1/topics/db/queries/#one-to-one-relationships)
* [Queries over related objects](https://docs.djangoproject.com/en/4.1/topics/db/queries/#queries-over-related-objects)




--------

## micro project - cafe project

* Create new project with django
* Create super user
* Create multi app and fill models.py fill with Cafe project ERD
* Add your model in to django admin

NOTE : change name  Users table to Customer


[sample model 1](https://docs.djangoproject.com/en/4.1/topics/db/queries/#making-queries)

[sample model 2](https://github.com/mustafamuratcoskun/django-blog-app/blob/master/article/models.py)

[sample model 3](https://github.com/mhsharifi96/django_repo/blob/main/myblog/post/models.py)

-------



  