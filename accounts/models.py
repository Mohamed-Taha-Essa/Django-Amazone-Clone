from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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
