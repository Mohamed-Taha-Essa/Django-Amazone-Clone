from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from utils.generate_code import generate_code
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , related_name = 'profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile')
    code = models.CharField( max_length=10 , default = generate_code)
    def __str__(self):
        return str(self.user)
    
@receiver(post_save , sender = User)
def create_profile(sender , instance,created ,**kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )



PHONE_TYPE=(
    ('Primary','Primary'),
    ('Secondary','Secondary'),
)
class ContactNumber(models.Model):
    user = models.ForeignKey(User , related_name = 'user_contacts', on_delete=models.CASCADE)
    type = models.CharField(max_length=15 ,choices = PHONE_TYPE)
    number = models.CharField( max_length=25)

ADDRESS_TYPE=(
    ('Home','Home'),
    ('Office','Office'),
    ('Bussiness','Bussiness'),
    ('Academy','Academy'),
    ('Others','Others'),
)

class Address(models.Model):
    user =models.ForeignKey(User, related_name='address_user', on_delete=models.CASCADE)
    address = models.CharField(max_length = 200)
    address_type = models.CharField(choices=ADDRESS_TYPE ,max_length=12)
