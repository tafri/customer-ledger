from django.db import models
from user.models import UserDetails

class AccountDetails(models.Model):
    owner = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=8, default=0.0)
