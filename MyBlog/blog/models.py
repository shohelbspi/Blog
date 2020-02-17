from django.db import models

# Create your models here.


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    Stmp = models.DateField(blank=True)
    image = models.ImageField(upload_to='images',default='')

    def __str__(self):
        return self.title
