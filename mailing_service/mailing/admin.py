from django.contrib import admin
from .models import Mailing, Client, Message

# Register your models here.


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ["beginning_date", "message", "gender_filter", "operator_code_filter", "ending_date"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["mobile_number", "name", "surname", "email", "tag", "timezone"]


@admin.register(Message)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["time_create", "sending_status", "mailing", "client"]
