from django.urls import path 
from . import views


urlpatterns = [
    path('',views.HabitList.as_view())
]
