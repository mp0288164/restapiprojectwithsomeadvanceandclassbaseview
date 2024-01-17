from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name=models.CharField(max_length=100)
    course_id=models.CharField(max_length=50)
    course_fees=models.IntegerField()

    def __str__(self):
        return self.course_name

class Student(models.Model):
    student_name=models.CharField(max_length=100)
    student_id=models.CharField(max_length=50)
    student_course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    address=models.CharField(max_length=300)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    def __str__(self):
        return "%s %s" %(self.student_name,self.student_course)