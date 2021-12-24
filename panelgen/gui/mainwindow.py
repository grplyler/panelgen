from PyQt5 import QtWidgets, uic
from pkg_resources import resource_filename
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uifile = resource_filename('panelgen.gui', 'mainwindow.ui')
        uic.loadUi(uifile, self)