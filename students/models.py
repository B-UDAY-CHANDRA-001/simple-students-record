from django.forms import ModelForm,Textarea
from django.db import models

class Students(models.Model):
    RollNo = models.IntegerField()
    Name = models.CharField(max_length=20)
    Branch = models.CharField(max_length=10)
    mark_1 = models.IntegerField()
    mark_2 = models.IntegerField()
    
class Meta:
    db_table = "students"
    

# Create your models here.
