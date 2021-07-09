from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """ Class serializers of the Token Obtain Pair model """

    @classmethod
    def get_token(cls, user):
        """
            Override of the get_token method,
            necessary to include the user name in the jwt token
        """

        token = super().get_token(user)

        token['user_name'] = f'{user.first_name} {user.last_name}'
        token['roles'] = list(map(lambda group: group.id, user.groups.all()))

        return token
