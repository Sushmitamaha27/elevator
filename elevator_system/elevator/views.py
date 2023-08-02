from django.shortcuts import render
from rest_framework import viewsets
from .models import Elevator, ElevatorRequest
from .serializers import ElevatorSerializer,ElevatorRequestSerializer



# Create your views here.
class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer


class ElevatorRequestViewSet(viewsets.ModelViewSet):
    queryset = ElevatorRequest.objects.all()
    serializer_class = ElevatorRequestSerializer