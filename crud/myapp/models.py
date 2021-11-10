from django.db import models
from django.forms import widgets

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=70)
    jersey_no = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)