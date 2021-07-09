from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .recipes import Recipes


class BaseTestCases:

    class BaseTest(TestCase):

        @classmethod
        def setUpClass(cls):
            """ Generic set up data for tests """

            ADMINISTRATOR_GROUP = Group.objects.get_or_create(
                name=settings.USER_GROUPS['ADMINISTRATOR'])

            cls.recipes = Recipes()
            cls.user = cls.recipes.user.make()
            cls.user.groups.add(ADMINISTRATOR_GROUP[0].id)
            cls.token = RefreshToken.for_user(cls.user).access_token
            super().setUpClass()

        def get_client(self, token=False):
            """
            Test method to request data from API authenticating using APIClient
            Arguments:
                - token (Token): User Token for client
            Returns:
                - client (API partial_situation Client): APIClient from drf test
            """

            if not token:
                token = self.token

            client = APIClient()
            client.credentials(
                HTTP_AUTHORIZATION='Bearer ' + str(token))
            return client

        def assert_data_creation(self, ModelClass):
            """ Test method to assert Model Data Creation """

            self.assertTrue(ModelClass.objects.count())

        def get_model_data(self, url):
            """ Test method to return model data from view """

            client = self.get_client()
            response = client.get(url)
            self.assertTrue(response)
            self.assertTrue(response.data)
            self.assertTrue(status.is_success(response.status_code))

        def get_model_anonymous(self, url):
            """ Test method to get model with anonymous user """

            client = APIClient()
            response = client.get(url)
            self.assertTrue(status.is_client_error(response.status_code))
