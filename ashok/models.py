from django.db import models
from django.db.models.fields import CharField

# Create your models here

class Person(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=122, null=True)
    post = models.CharField(max_length=122, null=True)
    desc = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=122, null=True)
    phone = models.CharField(max_length=122, null=True)
    location = models.CharField(max_length=122, null=True)

    def __str__(self):
        return self.name


class Social_links(models.Model):
    facebook = models.CharField(max_length=122, null=True)
    twitter = models.CharField(max_length=122, null=True)
    linkedin = models.CharField(max_length=122, null=True)
    youtube = models.CharField(max_length=122, null=True)

    def __str__(self):
        return self.facebook


class Projects(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=122, null=True)
    short_desc = models.CharField(max_length=200, null=True)
    full_desc = models.CharField(max_length=200, null=True)
       
    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

class Timeline(models.Model):
    date = models.DateField(null=True)  #this one
    topic = models.CharField(max_length=122)
    des = models.CharField(max_length=200)

    def __str__(self):
        return self.topic


class Services(models.Model):
    topic = models.CharField(max_length=122)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.topic

class Company(models.Model):
    info = models.CharField(max_length=200)
    name = models.CharField(max_length=122)
    post = models.CharField(max_length=122)

    def __str__(self):
        return self.info 

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    message = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name
