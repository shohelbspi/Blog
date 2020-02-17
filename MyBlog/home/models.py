from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    content = models.TextField()
    Stmp = models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    
    sno = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=255)
    member_work = models.CharField(max_length=255) 
    member_email = models.CharField(max_length=120)
    member_phone = models.CharField(max_length=20)
    member_content = models.TextField()
    member_image = models.ImageField(upload_to='images',default='')

    def __str__(self):
        return self.member_name

