from django.test import TestCase
from .models import Location, Image, Category

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='nairobi')
        self.location.save()

        self.category = Category(name ='food')
        self.category.save()

        self.image = Image( id = 1,name ='bg.jpg',description = 'good', category=self.category, location=self.location)



    def test_save(self):
        self.image
        self.image.image_save()
        self.assertTrue(len(Image.objects,all())>0)
