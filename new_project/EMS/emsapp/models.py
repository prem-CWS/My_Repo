from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=50,unique=True)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    salary=models.IntegerField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='employees')


    def __str__(self):
        return self.name 
        