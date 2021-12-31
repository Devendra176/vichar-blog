from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Registeruser(models.Model):
    #id = models.AutoField(primary_key=True)
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    # lname = models.CharField(max_length=50)
    # userslug = models.CharField(max_length=50,unique=True)
    # aboutperson = models.CharField(max_length=500,default='',blank=True)
    contact = models.CharField(max_length=15)
    email = models.EmailField(max_length=50,unique=True)
    # state = models.CharField(max_length=50)
    # city = models.CharField(max_length=20)
    
    aboutpro = models.CharField(max_length=500, default="", blank=True, null=True)
    aboutprofile = models.CharField(max_length=500, default="", blank=True, null=True)
    photo = models.ImageField(upload_to='profile/image', default="profile/image/icon.jpg",null=True)
    coverphoto = models.ImageField(upload_to='profile/image', default="profile/image/home-bg.jpg",null=True)
    timeStamp1 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Registeruser, on_delete=models.CASCADE)
    blogphoto = models.ImageField(upload_to='post/image', blank=True ,null=True)


    def __str__(self):
        return self.title


