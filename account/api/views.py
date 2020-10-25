from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.models import Account
from account.api.serializers import RegistrationSerializer


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered new user"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)

# @api_view(['GET'])
# def users_view(request):
#     if request.method == 'GET':
#         users = Account.objects.all()
#         serializers =