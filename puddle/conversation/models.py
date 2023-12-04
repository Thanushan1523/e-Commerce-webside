from django.db import models
from item.models import Item

# Create your models here.
class Conversation(models.Model):
    item=models.ForeignKey(Item, related_name='coversation',on_delete=models.CASCADE)