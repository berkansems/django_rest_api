from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    date=models.DateTimeField(auto_now=True,auto_now_add=False)




class Car(models.Model):
    company=models.CharField(max_length=30)
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
