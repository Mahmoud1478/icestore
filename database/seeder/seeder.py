from globals import AutoLoader


class Seeder:

    def seed(self):
        self.call("categories")

    @staticmethod
    def call(seeder):
        module = AutoLoader.seeder(seeder)
        module.run()
