from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

# Create your models here.
class Address(models.Model):
    user = models.ForeignKey('auth.User', default='', on_delete=models.CASCADE)
    name = models.CharField(max_length = 30,null=True, blank=True)
    address = models.CharField(max_length = 100,null=True, blank=True) 
    email_id = models.EmailField(max_length = 50, unique=True, null=True, blank=True)
    phone_number = models.CharField(_('number'), max_length=10 ,null=True, blank=True)  

    def __str__(self):
        return self.name


class AudioFile(models.Model):
    speech = models.CharField(max_length=255, blank=True)
    audio = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

