from django.test import TestCase

from macapa.models import MacapaContact

from .recipes import Recipes


class TestMacapaContactModel(TestCase):
    """ Test case for daily warning model """

    multi_db = True

    def setUp(self):
        """ Set up data for tests """

        self.recipes = Recipes()

    def test_contact_macapa_creation(self):
        """ Test contact macapa creation """

        total_items = MacapaContact.objects.count()
        self.recipes.macapa.make()
        self.assertTrue(MacapaContact.objects.count() == total_items + 1)

    def test_contact_macapa_save(self):
        """ Test get and post save macapa """

        macapa = self.recipes.macapa.make()
        macapa_latest = MacapaContact.objects.latest()

        self.assertEqual(macapa.nome, macapa_latest.nome)
        self.assertEqual(macapa.celular, macapa_latest.celular)
