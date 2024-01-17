from django.urls import path,include
from  . views  import CourseView,StudentView
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'courses',CourseView)
router.register(r'students',StudentView)
urlpatterns=[
    path('',include(router.urls)),
]