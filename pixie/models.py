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

    @classmethod
    def search_by_category(cls,search_term):
        result = cls.objects.filter(name__icontains=search_term).first()
        return result

class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 256)
    category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location)

    @classmethod
    def get_all(cls):
        photo = cls.objects.all()
        return photo

    @classmethod
    def get_image_by_category(cls,category):
        img = cls.objects.filter(category = category).all()
        return img
