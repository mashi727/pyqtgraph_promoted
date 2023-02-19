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
        self.plot_xy()

    def plot_xy(self):
        p1 = self.widget.addPlot(title="Basic array plotting", y=np.random.normal(size=100))
        self.widget.nextRow()
        p2 = self.widget.addPlot(title="Multiple curves")
        p2.plot(np.random.normal(size=100), pen=(255,0,0), name="Red curve")
        p2.plot(np.random.normal(size=110)+5, pen=(0,255,0), name="Green curve")
        p2.plot(np.random.normal(size=120)+10, pen=(0,0,255), name="Blue curve")
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__== '__main__':
    main()