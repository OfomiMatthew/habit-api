from django.shortcuts import render
from .models import Habit
from .serializers import HabitSerializer
from rest_framework import generics

# Create your views here.
class HabitList(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
