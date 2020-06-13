from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from .serializers import UserSerializer, AuthTokenSerializer


class UserPublicCreationView(generics.CreateAPIView):
    """
    User Public View (doesn't need authentication).
    Necesary for creating new users in the system.
    """
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        """
        Overwrites default ObtainAuthToken, to add the user information on the request.
        Returns:
            response: The default reponse, with user aditional information.
        """
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        response.data['user'] = {
            'name': token.user.name,
            'email': token.user.email
        }
        return response


class UserPrivateView(generics.RetrieveUpdateAPIView):
    """
    User private view, to deal with authenticated user actions.
    For now, they only can access and edit their own information.
    """
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
