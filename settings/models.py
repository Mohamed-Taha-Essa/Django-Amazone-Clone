from django.db import models

# Create your models here.

class Settings(models.Model):
    name = models.CharField( max_length=50)
    logo = models.ImageField(upload_to='settings')
    subtitle = models.TextField(max_length=500 )
    call_us = models.CharField( max_length=50)
    email_us = models.CharField( max_length=50)

    emails = models.TextField(max_length = 50)
    phones = models.TextField(max_length = 50)
    address = models.TextField(max_length = 100)

    android_app = models.URLField(null=True,blank=True)
    ios_app = models.URLField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    youtube = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)


    def __str__(self):
        return self.name
    

class DeliveryFee(models.Model):
    fee = models.IntegerField()

    def __str__(self):
        return str(self.fee)
    
    