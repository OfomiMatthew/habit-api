from django.db import models
from datetime import time


class Habit(models.Model):
  name= models.CharField(max_length=255)
  description = models.TextField()
  event_time = models.TimeField(default=time(7, 0)) 
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name
