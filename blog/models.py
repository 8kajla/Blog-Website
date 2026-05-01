from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email= models.EmailField()
    about_me = models.TextField()
    slug_author = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption= models.CharField(max_length=50)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title= models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    preview = models.TextField()
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.CharField(max_length=150)
    author= models.ForeignKey(Author , on_delete=models.SET_NULL, null=True)
    tag= models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comments(models.Model):
    user_name = models.CharField(max_length=250)
    email = models.EmailField()
    text = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')



