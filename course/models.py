from django.db import models
from teacher.models import Teacher

class Course(models.Model):
    name=models.CharField(max_length=50)
    # username = models.LowerCharField(max_length=128, lowercase=True, null=False, unique=True)
    # email=models.CIEmailField(max_length=70)
    duration_in_months=models.IntegerField()
    start_date=models.DateField()
    end_date=models.DateField()
    description=models.TextField(null=True)
    teacher=models.ForeignKey(Teacher,null=True,on_delete=models.CASCADE)


    
    def __str__(self):
    	return self.name
