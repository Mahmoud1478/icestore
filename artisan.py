from globals import AutoLoader
from vendor import App
import json
import time
import glob
import sys
import os


class Artisan:
    def __init__(self, sysArgs=None):
        self.args = sysArgs
        self.options = self.args[1:]
        self.FUNCTIONS_MAPPER = {
            "make": {
                "module": self.module,
                "model": self.model,
                "controller": self.controller,
                "migration": self.migration,
                "ui": self.ui,
                "seeder": self.seeder
            },
            "convert": {
                "qrc": self.convert_qrc,
                "ui": self.convert_ui,
            },
            "migrate": {
                "start": self.migrate,
                "fresh": self.migrate_fresh
            },
            "build": self.build,
            "exe": self.exe,
            "seed": self.seed
        }
        if ":" in self.args[0]:
            command, command_type = self.args[0].split(":")
            self.FUNCTIONS_MAPPER[command.lower()][command_type.lower()](self.options)
        else:
            self.FUNCTIONS_MAPPER[self.args[0].lower()](self.options)

    @staticmethod
    def module(options):

        with open("AppConfiguration.json", "r", encoding="utf8") as AppConfiguration:
            json_ = json.load(AppConfiguration)["Paths"]
            uiPath = json_["uiUserInterface"]
            modelsPath = json_["Modules"]
            AppConfiguration.close()

        name = options[0]
        module_path = f"{modelsPath}/{name}"
        module_path_ui = f"{uiPath}/{name}"
        if not os.path.isdir(module_path):
            os.mkdir(module_path)
            os.mkdir(f"{module_path}/ui")
            os.mkdir(f"{module_path}/models")
            os.mkdir(f"{module_path}/controllers")
            print(f"created {App.generateMainModel(name)}")
            print(f"created {App.generateMainController(name)}")
            with open(f"{module_path}/ui/{name.lower()}", "w", encoding="utf8"):
                pass
            print(f"created {module_path}/ui/{name.lower()}")
            if not os.path.isdir(module_path_ui):
                os.mkdir(module_path_ui)
                print(f"created {App.generateUi(name, 'widget')}")
        else:
            print("the module is already exists")

    @staticmethod
    def convert_qrc(*args):
        print("convert_qrc")

    @staticmethod
    def convert_ui(*args):
        print("convert_ui")

    @staticmethod
    def controller(options):
        name, module_name = options[0].split("@")
        print(f'''created {App.generateController(name, module_name)}''')

    @staticmethod
    def migration(options: list):
        print(f'''created {App.generateMigration(options[0])}''')

    @staticmethod
    def migrate(*args):

        with open("AppConfiguration.json", "r", encoding="utf8") as AppConfiguration:
            migrationsPath = json.load(AppConfiguration)["Paths"]["migrations"]
            AppConfiguration.close()

        files = glob.glob(f"{migrationsPath}/*.py")
        for item in files:
            start = time.time()
            name = str(item).split("\\")[-1].replace(".py", '')
            table = AutoLoader.migration(item)
            table.up()
            finish = time.time()
            print(f'''migrated {name} toke {finish - start :.3f} s ''')

    @staticmethod
    def un_migrate():

        with open("AppConfiguration.json", "r", encoding="utf8") as AppConfiguration:
            migrationsPath = json.load(AppConfiguration)["Paths"]["migrations"]
            AppConfiguration.close()

        files = glob.glob(f"{migrationsPath}/*.py")
        for item in files:
            start = time.time()
            name = str(item).split("\\")[-1].replace(".py", '')
            table = AutoLoader.migration(item)
            table.down()
            finish = time.time()
            print(f"dropped {str(name)}  toke {finish - start :.3f} s")

    @staticmethod
    def model(options: str):
        name, module_name = options[0].split("@")
        print(f'''created {App.generateModel(name, module_name)}''')

    def migrate_fresh(self, *args):
        self.un_migrate()
        self.migrate()

    def build(self, *args):
        pass

    def exe(self, *args):
        pass

    @staticmethod
    def ui(options):
        name, module = options[0].split("@")
        print(f'created {App.generateUi(name, options[1], module)}')

    @staticmethod
    def seeder(options):
        pass

    @staticmethod
    def seed(options):
        print("start seeding")
        start = time.time()
        name = "seeder"
        seeder = AutoLoader.mainSeeder(name)
        seeder.seed()
        finish = time.time()
        print(f"finish seeding  {finish - start :.3f} s")


if __name__ == '__main__':
    Artisan(sys.argv[1:])
