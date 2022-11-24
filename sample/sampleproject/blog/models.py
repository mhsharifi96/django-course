from django.db import models
from django.urls import reverse

# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model


"""class post(models.Model):
    # title
    # content
    # updated_at
    # published_at
    # category
    # """

class Author(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500,null  =True, blank=True)
    profile_picture = models.ImageField(blank=True)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    # thumbnail = models.ImageField(upload_to='images/category/%Y/%m/%d',blank=True,null=True)

    # def get_absolute_url(self): # new
    #     return reverse('blog:category')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='images/posts/%Y/%m/%d',null=True,blank=True) #upload_to='images/posts/%Y/%m/%d'
    categories = models.ManyToManyField(Category,blank=True,null=True)
    featured = models.BooleanField()
    STATUS  = [('en','enable'),('de','disable'),('da','draft')]
    status = models.CharField(max_length=2,choices=STATUS)

 


    def __str__(self):
        return self.title   

# https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    title  = models.CharField(max_length=254)
    content = models.CharField( max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta : 
        db_table = "comment"
        verbose_name = "comment"
        verbose_name_plural = "comments"
        # get_latest_by = "-created_at" #This specifies the default field(s) to use in your model Manager’s latest() and earliest() methods.
        ordering = ['-created_at']
