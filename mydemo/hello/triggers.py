from django.db.models.signals import post_save
from django.dispatch import receiver
from pip._internal.utils import datetime

from .models import Service, HistoryCost

@receiver(post_save, sender=Service)
def create_history_cost(sender, instance, **kwargs):
    if instance.id:
        old_cost = instance.cost
        new_cost = instance.cost
        HistoryCost.objects.create(service=instance, old_cost=old_cost, new_cost=new_cost, change_date=datetime.date.today())