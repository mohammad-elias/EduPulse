from django.contrib import admin
from .models import Authority,Institution,OtpToken
# Register your models here.

admin.site.register(Authority)
admin.site.register(Institution)
admin.site.register(OtpToken)