from unicodedata import name
from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    accumulative_amount = models.DecimalField(max_digits=20, decimal_places=8, default=0.0)