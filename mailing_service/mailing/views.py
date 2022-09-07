from django.shortcuts import render
from rest_framework import viewsets
from .models import Mailing
from .serializers import MailingSerializer

# Create your views here.


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

