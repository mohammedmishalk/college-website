from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from api.serializers import userSerializers

# Create your views here.
def home(request):
          return HttpResponse("ready")

class userViewsets(viewsets.ModelViewSet):
          queryset = User.objects.all()
          serializer_class = userSerializers