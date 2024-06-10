from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('features.urls')),
    path('contact_us/',include('contact.urls')),
    path('management/',include('management.urls')),
    path('institutions/',include('institute.urls')),
    path('transaction/',include('transaction.urls')),
]
