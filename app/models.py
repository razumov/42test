from django.db import models
from picklefield.fields import PickledObjectField


class Person(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    bio = models.TextField()
    contacts = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Request(models.Model):
    date = models.DateTimeField(auto_now=True)
    request = PickledObjectField()
    priority = models.IntegerField(default=0)
    
    
class LogModel(models.Model):
    date = models.DateTimeField(auto_now=True)
    model = models.CharField(max_length=40)
    action = models.CharField(max_length=15)
