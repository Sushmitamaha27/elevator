from django.db import models

class Elevator(models.Model):
    name = models.CharField(max_length=100)
    current_floor = models.IntegerField(default=1)
    is_moving = models.BooleanField(default=False)
    is_operational = models.BooleanField(default=True)

class ElevatorRequest(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE, related_name='requests')
    floor = models.IntegerField()
    direction = models.CharField(max_length=10)  # 'up' or 'down'
    created_at = models.DateTimeField(auto_now_add=True)
