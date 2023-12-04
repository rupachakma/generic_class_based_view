from django.http import HttpResponse
from django.shortcuts import render
from app.models import Item
from rest_framework import generics
from app.serializers import ItemSerializers

# Create your views here.
def home(request):
    return HttpResponse("hello")

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers
