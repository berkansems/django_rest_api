from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name= models.CharField(max_length=25)
    std_number=models.IntegerField()
    TEACHER = (
        ('ahmadi','Ahmadi'),
        ('shams','Shams'),
        ('sem','Sem')
    )
    teacher =models.CharField(max_length=6,choices=TEACHER)

