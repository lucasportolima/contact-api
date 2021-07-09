from model_mommy.recipe import Recipe

from varejao.models import VarejaoContact


class Recipes:

    def __init__(self):

        self.varejao = Recipe(VarejaoContact)
