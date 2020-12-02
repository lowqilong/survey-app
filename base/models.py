from django.db import models

# Create your models here.


class Post(models.Model):

    text = models.TextField()
    author = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)


class Person(models.Model):

    name = models.TextField()
