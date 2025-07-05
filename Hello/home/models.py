from django.db import models

# Create your models here.
class Contact(models.Model):
 name=models.CharField(max_length=100)
 email=models.EmailField()
 phone=models.CharField(max_length=15)
 address=models.TextField()
 contact = models.CharField(max_length=100)  
 message=models.TextField()
 date=models.DateTimeField()

 def __str__(self):
    return self.name
