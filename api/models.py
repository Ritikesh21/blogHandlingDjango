from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    owner = models.ForeignKey('auth.User', related_name='blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']