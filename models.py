from django.db import models
class Service(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_des=models.TextField()
    
class placed(models.Model):
    name=models.name = models.CharField(max_length=60)
    lname=models.name=models.CharField(max_length=60)
    ad = models.name=models.CharField(max_length=100)
    state = models.name=models.CharField(max_length=100)
    country = models.name=models.CharField(max_length=100)
    mail = models.name=models.CharField(max_length=100)
    ph = models.name=models.CharField(max_length=10)




    






# Create your models here.
