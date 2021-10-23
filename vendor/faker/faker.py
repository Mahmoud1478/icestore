from random import *
from vendor.faker.assets.assets import FakerAssets
from vendor.faker.assets.resources import FakerResources


class Faker:
    @staticmethod
    def fullName(nameCount: int, male: bool = True, female: bool = True):
        fullName = ""
        fName = FakerResources.malesFemalesNames
        if male:
            fName = FakerResources.males
        if female:
            fName = FakerResources.females
        lName = FakerResources.lName
        middleName = FakerResources.males
        for i in range(nameCount - 1):
            if i == 0:
                fullName += choice(fName)
            else:
                fullName += f" {choice(middleName)}"
        return fullName + " " + choice(lName)

    @staticmethod
    def fName(male: bool = True, female: bool = True):
        fName = FakerResources.malesFemalesNames
        if female and not male:
            fName = FakerResources.females
        if male and not female:
            fName = FakerResources.males
        return choice(fName)

    @staticmethod
    def lName():
        lName = FakerResources.lName
        return choice(lName)

    @staticmethod
    def integer(start: int, end: int):
        return randint(start, end)

    @staticmethod
    def username():
        source = FakerResources.malesFemalesNames
        return choice(source) + "".join([str(randint(0, 9)) for _ in range(4)])

    @staticmethod
    def phone(size: int = 11):
        prefix = "01"
        return prefix + "".join([str(randint(0, 9)) for _ in range(size - 2)])

    @staticmethod
    def text(size: int):
        source = FakerResources.text
        text = ""
        status = False
        counter = 0
        while not status:
            for char in source:
                if counter >= size:
                    status = True
                else:
                    text += char
                    counter += 1

        return text

    @staticmethod
    def writeFile():
        with open("vendor/faker/assets/resources.py", "w", encoding="utf8") as resource:
            malesFemalesNames = FakerAssets.FIRST_MALE_NAMES + FakerAssets.FIRST_FEMALE_NAMES
            males = FakerAssets.FIRST_MALE_NAMES
            females = FakerAssets.FIRST_FEMALE_NAMES
            lName = FakerAssets.LAST_NAMES
            shuffle(males)
            shuffle(females)
            shuffle(malesFemalesNames)
            shuffle(lName)
            resource.write(f'''class FakerResources:
    malesFemalesNames = {malesFemalesNames}
    males = {males}
    females = {females}
    lName = {lName}
    text = '{FakerAssets.TEXT_FIELD}'
    email = {FakerAssets.EMAILS}
    ''')
