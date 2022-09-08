from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Mailing

@receiver(post_save, sender=Mailing)
def function(sender, **kwargs):
    print("Рассылка создана")