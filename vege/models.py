from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Recipe(models.Model) : 
    user = models.ForeignKey(User , on_delete = models.SET_NULL , null = True , blank = True)
    recipeName = models.CharField(max_length=100)
    recipeDescription = models.TextField()
    recipeImage = models.FileField(upload_to="recipe" , null = True)
    recipeViewCount = models.IntegerField(default = 1)
    
class Department(models.Model) : 
    department = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.department
    
    class Meta: 
        ordering = ['department']


class StudentID(models.Model) : 
    studentId = models.CharField(max_length = 100)
    def __str__(self) -> str:
        return self.studentId

class Student(models.Model):
    department = models.ForeignKey(Department, related_name="students", on_delete=models.CASCADE)
    studentid = models.OneToOneField(StudentID, related_name="student", on_delete=models.CASCADE)
    studentName = models.CharField(max_length=100)
    studentEmail = models.EmailField(unique=True)
    studentAge = models.IntegerField(default=18)
    studentAddress = models.TextField()

    def __str__(self) -> str:
        return self.studentName

    class Meta:
        ordering = ['studentName']
        verbose_name = "student"

        
        



    
                

