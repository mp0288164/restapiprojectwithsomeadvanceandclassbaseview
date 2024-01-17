from django.contrib import admin
from .models import Courses,Student
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    List_display=('course_id','course_name','course_fees')
    search_fields=('course_name',)

class StudentAdmin(admin.ModelAdmin):
    List_display=('student_id','student_name','student_course','about','address','phone')
    List_filter=['student_name','student_course']

admin.site.register(Courses,CourseAdmin)
admin.site.register(Student,StudentAdmin)

