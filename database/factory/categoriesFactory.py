from vendor import Faker


class CategoriesFactory:
    @staticmethod
    def make(times):
        # "key" : [value for _ in range(times) ],
        # unique_key :  Faker().unique("field", times),
        return {
            "name": Faker().unique("fName", times),
        }
