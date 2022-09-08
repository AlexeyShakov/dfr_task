from rest_framework import serializers
from .models import Mailing, Client


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = "__all__"


class Clientserializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
