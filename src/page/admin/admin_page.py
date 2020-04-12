from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget
from PyQt5 import uic

import resource
from page.admin.admin_navbar import getNavBarAdmin


def initAdminPage(window, adminName):
  global _navbar_A, _content_A_1
  # Load ui
  uifile = QFile(":ui/ui/admin/admin_layout.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, window)
  uifile.close()
  # Get object from layout ui
  _mainVLayout_A = window.findChild(QVBoxLayout, "mainVLayout_A")

  #load navbar widget
  _navbar_A = getNavBarAdmin()
  
  #load content
  _content_A_1 = QWidget()
  uifile = QFile(":ui/ui/admin/admin_content_dashboard.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, _content_A_1)
  uifile.close()

  #set admin name and image to default
  _adminName_A_1 = _content_A_1.findChild(QLabel, "adminName")
  _adminImage_A_1 = _content_A_1.findChild(QLabel, "adminImage")
  _adminName_A_1.setText(adminName)
  pixmap = QPixmap(":img/img/profil_default.png")
  pixmap = pixmap.scaledToHeight(200)
  _adminImage_A_1.setPixmap(pixmap)

  #Load widgets to layout
  _mainVLayout_A.addWidget(_navbar_A)
  _mainVLayout_A.addWidget(_content_A_1)
  _navbar_A.setFixedHeight(200)


  # # # Load layout ui
  # # uifile = QFile(":ui/ui/dosen_layout.ui")
  # # uifile.open(QFile.ReadOnly)
  # # uic.loadUi(uifile, window)
  # # uifile.close()
  # # # Get object from layout ui
  # # _mainVLayout_D_1 = window.findChild(QVBoxLayout, "mainVLayout_D_1")

  # # # Create and load navbar widget
  # # _navbar_D_1 = QWidget()
  # # uifile = QFile(":ui/ui/dosen_navbar.ui")
  # # uifile.open(QFile.ReadOnly)
  # # uic.loadUi(uifile, _navbar_D_1)
  # # uifile.close()
  # # # Get object from navbar ui
  # # _logoSiak_D_2 = _navbar_D_1.findChild(QLabel, "logoSiak_D_2")
  # # _berandaButton_D_2 = _navbar_D_1.findChild(QPushButton, "berandaButton_D_2")
  # # _pengaturanButton_D_2 = _navbar_D_1.findChild(QPushButton, "pengaturanButton_D_2")
  # # _buatAkunMhsButton_D_2 = _navbar_D_1.findChild(QPushButton, "buatAkunMhsButton_D_2")
  # # Asserting object findChild successful
  # # assert _berandaButton_D_2 is not None
  # # assert _pengaturanButton_D_2 is not None
  # # assert _buatAkunMhsButton_D_2 is not None
  # # Set logo
  # # _logoSiak_D_2.setPixmap(QPixmap(":img/img/logo_siak_full.png"))

  # # Create and load content dashboard widget
  # # Set widgets to layout
  # _mainVLayout_D_1.addWidget(_navbar_D_1)
  # _mainVLayout_D_1.addWidget(_content_D_1)
  # _navbar_D_1.setFixedHeight(200)
  # _content_D_1.setMinimumHeight(window.frameGeometry().height() - 200)

  # # Set connection
  # _berandaButton_D_2.clicked.connect(lambda: berandaButtonClicked())
  # _pengaturanButton_D_2.clicked.connect(lambda: pengaturanButtonClicked())
  # _buatAkunMhsButton_D_2.clicked.connect(lambda: buatAkunMhsButtonClicked())
