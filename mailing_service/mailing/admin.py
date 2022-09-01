from django.contrib import admin
from .models import Mailing, Client

# Register your models here.
admin.site.register(Mailing)
admin.site.register(Client)