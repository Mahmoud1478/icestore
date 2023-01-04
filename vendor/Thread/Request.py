from typing import Union

from PyQt5.QtCore import QThread, pyqtSignal

import re


class Request(QThread):
    response = pyqtSignal(dict)

    def __init__(self, function):
        super(Request, self).__init__()
        self.function = function

    def run(self):
        try:
            data = self.function()

            self.response.emit({
                "data": data,
                "massage": 'success',
                'status': True
            })
        except Exception as e:
            self.response.emit({
                "data": '',
                "massage": str(e),
                'status': False
            })
