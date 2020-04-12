from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5 import uic

import resource
# from util.mysql_controller import execQuery


def initDosenPage(window, auth):
    global _navbar_D_1, _content_D_1
    # Load layout ui
    uifile = QFile(":ui/ui/dosen_layout.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, window)
    uifile.close()
    # Get object from layout ui
    _mainVLayout_D_1 = window.findChild(QVBoxLayout, "mainVLayout_D_1")

    # Crate and load navbar widget
    _navbar_D_1 = QWidget()
    uifile = QFile(":ui/ui/dosen_navbar.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, _navbar_D_1)
    uifile.close()

    # Crate and load content dashboard widget
    _content_D_1 = QWidget()
    uifile = QFile(":ui/ui/dosen_content_dashboard.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, _content_D_1)
    uifile.close()

    # Set widgets to layout
    _mainVLayout_D_1.addWidget(_navbar_D_1)
    _mainVLayout_D_1.addWidget(_content_D_1)
    _navbar_D_1.setFixedHeight(200)
    _content_D_1.setMinimumHeight(window.frameGeometry().height() - 200)


    # # Asserting object findChild successful
    # assert _loginBgLabel_L_2 is not None
    # assert _usernameInput_L_2 is not None
    # assert _emailInput_L_2 is not None
    # assert _sendEmailButton_L_2 is not None
    # # Set connection
    # _sendEmailButton_L_2.clicked.connect(lambda: sendEmailButtonClicked(window))
