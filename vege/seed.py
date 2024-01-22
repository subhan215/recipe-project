from faker import Faker

fake = Faker()
import random
from .models import *
def seed_db(n = 10) -> None: 
    try: 

      for _ in range(n):
        departmentObjects = Department.objects.all()
        randomInd = random.randint(0 , len(departmentObjects) - 1)
        department = departmentObjects[randomInd]
        studentId = f'st{random.randint(100  ,999)}'
        studentName = fake.name()
        studentEmail = fake.email()
        studentAge = random.randint(1 , 99)
        studentAddress = fake.address()

        studentIdObj  =StudentID.objects.create(studentId = studentId)

        studentObj = Student.objects.create(
            department = department , 
            studentid = studentIdObj , 
            studentName = studentName , 
            studentEmail = studentEmail  ,
            studentAge = studentAge , 
            studentAddress = studentAddress
        )

    except Exception as e: 
       print(e)     

        