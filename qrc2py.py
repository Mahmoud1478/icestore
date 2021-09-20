import os
from inc.converters.QrcConvertor import Qrc


class QrcToPy(Qrc):
    def __init__(self):
        super(QrcToPy, self).__init__()
        self.convert()


QrcToPy()
