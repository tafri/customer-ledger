import decimal
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.models import AccountDetails

@api_view(["POST"])
def transaction(request, *args, **kwargs):
    '''
    DRF api view
    '''
    data = request.data
    data['amount'] = decimal.Decimal(data['amount'])
    creditor = AccountDetails.objects.get(pk=data.get('credit_account_id'))
    debitor = AccountDetails.objects.get(pk=data.get('debit_account_id'))
    if data.get('amount') <= debitor.amount:
        debitor.amount -= data.get('amount')
        creditor.amount += data.get('amount')
        debitor.save()
        creditor.save()
    if creditor.id != debitor.id:
        creditor.owner.accumulative_amount += data.get('amount')
        debitor.owner.accumulative_amount -= data.get('amount')
        creditor.owner.save()
        debitor.owner.save()
    return Response(data)