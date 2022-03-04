from django.db import models


# Create your models here.

class places(models.Model):
    place_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class travelblog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_img = models.ImageField(upload_to='blog_image')
    blog_desc = models.TextField()
