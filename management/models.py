from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import AuthorityUserManager
from django.conf import settings
import secrets

# Create your models here.

class Institution(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    logo = models.URLField(max_length=200)
    phone = models.CharField(max_length=20)
    students = models.IntegerField(default=0)
    created_by = models.ForeignKey('Authority',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Authority(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, blank=True)
    institutions = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True, blank=True)
    plan = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = AuthorityUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


def generate_otp():
    return str(secrets.randbelow(900000) + 100000)


class OtpToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="otps")
    otp_code = models.CharField(max_length=6, default=generate_otp)
    tp_created_at = models.DateTimeField(auto_now_add=True)
    otp_expires_at = models.DateTimeField(blank=True, null=True)
    
    
    def __str__(self):
        return self.user.email
    

    