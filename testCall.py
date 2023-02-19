import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QSizePolicy
import os

from pyqtgraph.dockarea.Dock import Dock
from pyqtgraph.dockarea.DockArea import DockArea

from PySide6.QtWebEngineWidgets import QWebEngineView
# Key Event
from PySide6.QtCore import Qt
import pyqtgraph as pg
from pyqtgraph import GraphicsLayoutWidget

# folium issues
import io
import folium
from folium import plugins

import numpy as np

from testui_nopro import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.widget = GraphicsLayoutWidget(self.centralwidget)

        # 中心座標 日本緯度経度原点
        center = [35.6580992222, 139.7413574722]
        #center = ['35.70643785143693', '139.5658181820346']
        # 地図作成
        m = folium.Map(
            location=center,
            zoom_start=18,
            tiles='https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png', # 通常
            #tiles='https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png', # 淡色
            #tiles='https://cyberjapandata.gsi.go.jp/xyz/ort/{z}/{x}/{y}.jpg', # 航空写真
            #tiles='https://cyberjapandata.gsi.go.jp/xyz/ort_old10/{z}/{x}/{y}.png', # 国土地理院 空中写真（1961～1964年）
            #attr='国土地理院 空中写真（1961～1964年）',
            attr='&copy; <ahref="https://maps.gsi.go.jp/development/ichiran.html">国土地理院</a>'
        )
        folium.Marker(center, popup="日本緯度経度原点",).add_to(m)
        # 折り畳み式ミニマップを追加
        plugins.MiniMap(toggle_display=True).add_to(m)
        data = io.BytesIO()
        m.save(data, close_file=False)
        #self.layout = QHBoxLayout()
        self.mapview = QWebEngineView()
        #self.layout.addWidget(self.mapview)
        #self.widget.setLayout(self.layout)
        self.mapview.setHtml(data.getvalue().decode())

        # Location of Graph
        # addWidget row: int, column: int, rowSpan: int, columnSpan: int
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        # Location of Map
        self.gridLayout.addWidget(self.mapview, 2, 0, 1, 1)
        self.setGeometry(50, 50, 1200, 1280) # WQXGA (Wide-QXGA)


        self.area = DockArea()
        d1 = Dock("Dock1")
        self.area.addDock(d1, 'left')      ## place d1 at left edge of dock area (it will fill the whole space since there are no other docks yet)
        w4 = pg.PlotWidget(title="Dock 4 plot")
        w4.plot(np.random.normal(size=100))
        d1.addWidget(w4)
        self.gridLayout.addWidget(self.area, 3, 0, 1, 1)
    
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