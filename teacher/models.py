from django.db import models
import datetime

class Teacher(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=20)
    county_from=models.CharField(max_length=15)
    id_number=models.CharField(max_length=8)
    email=models.EmailField(max_length=70)
    phone_number=models.CharField(max_length=10)
    subjects_teaching=models.CharField(max_length=70)
    years_of_experience=models.CharField(max_length=2)
    profession=models.CharField(max_length=90,null=True)    
