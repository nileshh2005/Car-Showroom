from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    email=models.EmailField()
    number=models.PositiveBigIntegerField()
    status=models.BooleanField(default=True)
    
class Registration(models.Model):
    Registration_First_Name=models.CharField(max_length=50)
    Registration_Last_Name=models.CharField(max_length=50)
    Registration_city=models.CharField(max_length=50)
    Registration_email=models.EmailField()
    Registration_number=models.PositiveBigIntegerField()
    Registration_password=models.CharField(max_length=8)
    Registration_confirm_password=models.CharField(max_length=8)
    status=models.BooleanField(default=True)