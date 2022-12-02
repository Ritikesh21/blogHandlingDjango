from django.db import models

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    number = models.IntegerField(blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self) -> str:
        return self.firstName