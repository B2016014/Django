from django.db import models

# Create your models here.
class booking(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    guest=models.IntegerField()
    comment=models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name+' '+self.last_name
    
class menu(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    description=models.CharField(max_length=2000)

    def __str__(self):
        return self.name
