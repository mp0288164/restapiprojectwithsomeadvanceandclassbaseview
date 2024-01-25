from django.shortcuts import render
from rest_framework import viewsets
from .models import Courses,Student
from . serializer import CourseSerializer,StudentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class CourseView(viewsets.ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializer
    #courses/courseid/students
    @action(detail=True,methods=['get'])
    def students(self,request,pk=None):
    
        course=Courses.objects.get(pk=pk)
        stu=Student.objects.filter(student_course=course)
        stu_serializer=StudentSerializer(stu,many=True,context={'request':request})
        return Response(stu_serializer.data)
        
        

class StudentView(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer