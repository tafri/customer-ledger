from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import UserDetails

@api_view(["GET"])
def user_details(request, *args, **kwargs):
    '''
    DRF api view
    '''
    user_id = request.data.get('user_id')
    if not user_id:
        user_id = kwargs.get('pk')
    model_data = UserDetails.objects.filter(pk=user_id)[0]
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'name', 'accumulative_amount'])
    return Response(data)