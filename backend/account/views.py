from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.models import AccountDetails

@api_view(["GET"])
def account_details(request, *args, **kwargs):
    '''
    DRF api view
    '''
    account_id = request.data.get('account_id')
    if not account_id:
        account_id = kwargs.get('pk')
    model_data = AccountDetails.objects.filter(pk=account_id)[0]
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'owner', 'amount'])
    return Response(data)