from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Image(models.Model):
    #image =
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 256)
    category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location, default = True)
