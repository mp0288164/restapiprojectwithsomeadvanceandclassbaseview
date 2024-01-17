from rest_framework import serializers
from . models import Courses,Student
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Courses
        fields="__all__"
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
