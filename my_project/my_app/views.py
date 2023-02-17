from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# Create your views here.
