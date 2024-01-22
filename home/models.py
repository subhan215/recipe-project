from django.db import models

class Student(models.Model) : 
    #id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null = True , blank = True)

class Car(models.Model) : 
    carName = models.CharField(max_length=500)
    speed = models.IntegerField(default = 50)
    def __str__(self) -> str: 
        return self.carName

# Create your models here.
