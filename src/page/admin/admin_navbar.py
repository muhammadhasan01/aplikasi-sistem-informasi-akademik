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
    return _navbar_A