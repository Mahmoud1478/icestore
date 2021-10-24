import json

with open("AppConfiguration.json", "r", encoding="utf8") as AppConfiguration:
    CONFIG = json.load(AppConfiguration)
    PyQtVersion = CONFIG["PyQtVersion"]


class App:

    @staticmethod
    def generateUi(path: str, name: str):
        with open(f"{path}/{name}.ui", "w", encoding="utf8") as uiFile:
            uiFile.write(f'''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="{name}">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>{CONFIG["MyAppName"]}</string>
  </property>
 </widget>
 <resources/>
 <connections/>
</ui>''')

    @staticmethod
    def generateMainController():
        pass

    @staticmethod
    def generateController():
        pass

    @staticmethod
    def generateModel():
        pass

    @staticmethod
    def generateMigration():
        pass
