from django.db import models

# Create your models here.
class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image_url = models.URLField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Plan(models.Model):
    type = models.CharField(max_length=40)
    description = models.CharField(max_length=50)
    price = models.IntegerField()
    features = models.JSONField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.type
    
    

