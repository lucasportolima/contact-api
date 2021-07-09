from django.test import TestCase

from varejao.models import VarejaoContact

from .recipes import Recipes


class TestVarejaoContactModel(TestCase):
    """ Test case for contact varejao model """

    multi_db = True

    def setUp(self):
        """ Set up data for tests """

        self.recipes = Recipes()

    def test_contact_varejao_creation(self):
        """ Test contact varejao creation """

        total_items = VarejaoContact.objects.count()
        self.recipes.varejao.make()
        self.assertTrue(VarejaoContact.objects.count() == total_items + 1)

    def test_contact_varejao_post_save(self):
        """ Test get and post save contact varejao """

        varejao = self.recipes.varejao.make()
        varejao_latest = VarejaoContact.objects.latest()

        self.assertEqual(varejao.nome, varejao_latest.nome)
        self.assertEqual(varejao.celular, varejao_latest.celular)
