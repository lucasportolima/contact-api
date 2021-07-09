from model_mommy.recipe import Recipe

from django.contrib.auth.models import User


class Recipes:

    def __init__(self):

        self.user = Recipe(User, is_staff=True)
