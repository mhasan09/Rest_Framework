from django.shortcuts import render
from rest_framework import viewsets
from .models import inventory
from .serializers import invertorySerializers

# Create your views here.
class inventoryView(viewsets.ModelViewSet):
    queryset = inventory.objects.all()
    serializer_class = invertorySerializers