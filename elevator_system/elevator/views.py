from django.shortcuts import render
from rest_framework import viewsets
from .models import Elevator, ElevatorRequest


# Create your views here.
class ElevatorViewSet(viewsets.ModelViewSet):
    pass


class ElevatorRequestViewSet(viewsets.ModelViewSet):
    pass