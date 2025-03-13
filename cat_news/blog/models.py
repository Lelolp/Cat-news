from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    picture = models.ImageField(upload_to='images/', blank=True)