from django.urls import path
from .views import *

urlpatterns = [
    path('api/students/',StudentDetails.as_view(),name='student_details'),
    path('api/students/<int:pk>/', StudentDetails.as_view(), name='student_details')

]