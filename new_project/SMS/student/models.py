from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mno=models.CharField(max_length=10)
    mail=models.EmailField()
    address=models.CharField(max_length=30)
    course=models.CharField(max_length=50)

    def __str__(self):
        return self.name