from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from pkg_resources import resource_filename
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, gen):
        super(MainWindow, self).__init__()
        self.gen = gen
        uifile = resource_filename('panelgen.gui', 'mainwindow.ui')
        uic.loadUi(uifile, self)

        self.generateButton.clicked.connect(self.onGenerate)
        
        # Panel Settings
        self.panel_count.valueChanged.connect(self.onPanelCountChanged)

    def onPanelCountChanged(self, value):
        print("count changed:", value)
        print("old value:", self.gen.cnf.base.count)
        self.gen.cnf.base.count = value
        print("new value:", self.gen.cnf.base.count)


    def onGenerate(self):
        # Generate
        print("Generating...")
        self.gen.generate('panel')

        # Load image
        pix = QPixmap('out.png')
        w = self.displayLabel.width()
        h = self.displayLabel.height()
        self.displayLabel.setPixmap(pix.scaled(w, h, Qt.KeepAspectRatio))
        print("Generate clicked.")