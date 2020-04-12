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

def berandaButtonClicked(window):
    uifile = QFile(":ui/ui/admin/admin_content_dashboard.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, window)
    uifile.close()
    global _content_D_1, _mainVLayout_D_1
    # Create new widget
    # newWidget = QWidget()
    # uifile = QFile(":ui/ui/dosen_content_dashboard.ui")
    # uifile.open(QFile.ReadOnly)
    # uic.loadUi(uifile, newWidget)
    # uifile.close()
    # setupDashboardContent(newWidget, auth)
    # # Set up the new widget
    # _mainVLayout_D_1.removeWidget(_content_D_1)
    # _content_D_1 = newWidget
    # _mainVLayout_D_1.addWidget(_content_D_1)

def userButtonClicked(window):
  pass

def matkulButtonClicked(window):
  pass