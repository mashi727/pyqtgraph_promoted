import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication
import os


# Key Event
from PySide6.QtCore import Qt
import pyqtgraph as pg

import numpy as np

from testui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__== '__main__':
    main()