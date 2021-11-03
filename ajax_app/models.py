from django.db import models
from django.shortcuts import render

# Create your models here.

class TestAjax(models.Model):
    name = models.CharField(max_length=25)
    family = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
