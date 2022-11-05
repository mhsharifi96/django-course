from django.db import models

class Author(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500,blank=True,null=True)
    profile_picture = models.ImageField(blank=True)

    class Meta :
        order = ['first_name']


    def __str__(self):
        return self.first_name


class Category(models.Model):
    title = models.CharField(' this is versbose ',max_length=20,help_text= "this is help text")
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField(blank=True)
    sample_number = models.IntegerField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null= True,blank= True)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    STATUS  = [('en','enable'),('de','disable'),('da','draft')]
    status = models.CharField(max_length=2,choices=STATUS)


    def __str__(self):
        return self.title  









