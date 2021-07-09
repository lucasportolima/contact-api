import json

from django.urls import reverse
from rest_framework import status

from macapa.models import MacapaContact
from core.tests.test_views import BaseTestCases

from .recipes import Recipes

CONTACT_PAYLOAD = {
    "nome": "MercaFacil",
    "celular": "5561123456789"
}


class TestMacapaView(BaseTestCases.BaseTest):
    multi_db = True

    def setUp(self):
        """ Set up data for tests """

        self.recipes = Recipes()
        self.url = reverse("macapa:macapa_contact-list")
        self.recipes.macapa.make()

    def test_assert_data_creation(self):
        """ Test method to assert contact macapa Data Creation """

        self.assert_data_creation(MacapaContact)

    def test_get_contact_macapa_data(self):
        """ Test method to return contact macapa data from view """

        self.get_model_data(self.url)

    def test_get_contact_macapa_anonymous(self):
        """ Test method to get contact macapa with anonymous user """

        self.get_model_anonymous(self.url)

    def test_post_create_contact_macapa_data(self):
        """ Test method to create and return contact macapa data without relations"""

        client = self.get_client()
        response = client.post(self.url,
                               json.dumps(CONTACT_PAYLOAD),
                               content_type="application/json")
        self.assertTrue(response)
        self.assertTrue(response.data)
        self.assertTrue(status.is_success(response.status_code))

        response = client.get(
            self.url, {
                'search_field': CONTACT_PAYLOAD['nome']
            }, format='json'
        )

        self.assertTrue(response)
        self.assertTrue(response.data)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEquals(response.data.get('count'), 1)

    def test_patch_update_contact_macapa_data(self):
        """ Test method to update contact macapa"""

        payload = {
            "nome": "MercaFacilAlterado"
        }

        client = self.get_client()
        response = client.get(self.url, format='json')
        response = response.data.get('results')[0].get('id')
        response = client.patch(f'{self.url}{response}/',
                                json.dumps(payload),
                                content_type="application/json")

        self.assertTrue(response)
        self.assertTrue(response.data)
        self.assertTrue(status.is_success(response.status_code))

        macapa_updated = MacapaContact.objects.get(
            id=response.data['id'])

        self.assertEquals(macapa_updated.nome, payload['nome'].upper())
