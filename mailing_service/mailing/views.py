from django.shortcuts import render
from rest_framework import viewsets
from .models import Mailing, Client
from .serializers import MailingSerializer, Clientserializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    @staticmethod
    @action(methods=["get"], detail=False)
    def general_statistic(request):
        """
        Данный метод делает статистику по всем рассылкам и отправленным сообщениям.
        """
        return Response({"detail": "Метод работает"})

    def detailed_statistic(self):
        """
        Данный делает детальную статистику по одной рассылке
        """
        pass


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = Clientserializer







