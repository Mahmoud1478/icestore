from globals import AutoLoader
from database.factory.categoriesFactory import CategoriesFactory
from modules.categories.models.categoriesModel import Categories


class CategoriesSeeder:
    def __init__(self):
        self.model = Categories()

    def run(self):
        self.model.createMany(**CategoriesFactory.make(500)).saveMany()
