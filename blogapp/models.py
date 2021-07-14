from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=70)
    body=models.TextField()   
    date=models.DateTimeField(auto_now_add=True)
    img =models.ImageField('',upload_to = 'images/')
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    fullname =models.CharField(max_length=70)
    email=models.EmailField()   
    message=models.TextField()
    
    
    def __str__(self):
        return self.fullname
