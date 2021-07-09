from model_mommy.recipe import Recipe

from macapa.models import MacapaContact


class Recipes:

    def __init__(self):

        self.macapa = Recipe(MacapaContact)
