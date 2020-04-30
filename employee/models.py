from django.db import models


class Employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    salary=models.IntegerField()
    post = models.CharField(max_length=40)
    created_at=models.DateTimeField(null=True,blank=True)
    updated_at=models.DateTimeField(null=True,blank=True)
