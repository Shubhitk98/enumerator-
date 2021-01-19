from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)  
    email = models.EmailField()  
    password = models.CharField(max_length=100) 
    confirm_password = models.CharField(max_length=100) 
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  

