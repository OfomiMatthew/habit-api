from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    event_time = serializers.SerializerMethodField()

    class Meta:
        model = Habit
        fields = ['name', 'description', 'event_time']

    def get_event_time(self, obj):
        return obj.event_time.strftime("%H:%M")  # Formats time to "HH:MM"
