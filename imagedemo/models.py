from django.db import models
from django.forms import ImageField


# model with images using imagefield
class Products(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    image=models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url=self.image.url
        except:
            url=""
        return url

# model with images using filefield
class NewProducts(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    image=models.FileField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.name


    
