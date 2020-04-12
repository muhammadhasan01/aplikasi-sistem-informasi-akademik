from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5 import uic

import resource
from page.admin.header import getNavBarAdmin


def initAdminPage(window, adminName):
  global _navbar_A, _content_A_1
  # Load ui
  header = getNavBarAdmin()
  uifile = QFile(":ui/ui/admin/mainpageadmin.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, window)
  uifile.close()
  # Get object from ui
  _adminName_A_1 = window.findChild(QLabel, "adminName")
  _adminName_A_1.setText(adminName)
