from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QWidget
from PyQt5 import uic

import resource

def getNavBarAdmin():
    # Load ui
    _navbar_A = QWidget()
    uifile = QFile(":ui/ui/admin/admin_navbar.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, _navbar_A)
    uifile.close()
    # Get object from ui
    _berandaButton_A = _navbar_A.findChild(QPushButton, "berandaButton")
    _userButton_A = _navbar_A.findChild(QPushButton, "userButton")
    _matkulButton_A = _navbar_A.findChild(QPushButton, "matkulButton")
    # Set connection
    _berandaButton_A.clicked.connect(lambda: berandaButtonClicked(window))
    _userButton_A.clicked.connect(lambda: userButtonClicked(window))
    _matkulButton_A.clicked.connect(lambda: matkulButtonClicked(window))
    
    return _navbar_A

def berandaButtonClicked(window):
    uifile = QFile(":ui/ui/admin/mainpageadmin.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, window)
    uifile.close()

def userButtonClicked(window):
  pass

def matkulButtonClicked(window):
  pass