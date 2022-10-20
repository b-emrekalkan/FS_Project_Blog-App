from rest_framework import generics, status
from django.conf import settings
from user.api.serializers import RegisterSerializer, UpdateUserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user.models import User
from django.contrib.auth import get_user_model
# User = settings.AUTH_USER_MODEL
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    #! We override the create() method so that the Token created with signal can return with data when the user registers. 👇
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        if Token.objects.filter(user=user):
            token = Token.objects.get(user=user)
            data['token'] = token.key
        else:
            data['error'] = 'User does not have token . Try again ...'
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

class UpdateUserView(generics.RetrieveUpdateAPIView):
    #! We used RetrieveUpdateAPIView so that the user can only update. 👆
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer