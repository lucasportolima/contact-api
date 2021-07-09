from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer


class AuthModelMixedIn:
    """ Default class for authentication """

    permission_classes = (IsAuthenticated,)


class MyTokenObtainPairView(TokenObtainPairView):
    """ Custom Token Obtain Pair view """

    serializer_class = MyTokenObtainPairSerializer
