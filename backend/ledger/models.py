from django.db import models
from account.models import AccountDetails

class LedgerDetails(models.Model):
    creditor = models.ForeignKey(AccountDetails, on_delete=models.DO_NOTHING, related_name='creditor')
    debitor = models.ForeignKey(AccountDetails, on_delete=models.DO_NOTHING, related_name='debitor')
    amount = models.DecimalField(max_digits=20, decimal_places=8, default=0.0)
