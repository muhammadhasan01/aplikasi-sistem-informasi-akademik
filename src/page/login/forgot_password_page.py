from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5 import uic

import resource


def initForgotPasswordPage(window):
    global _usernameInput, _emailInput, _sendEmailButton
    # Load ui
    uifile = QFile(":ui/ui/forgot_password_page.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, window)
    uifile.close()
    # Get object from ui
    _forgotPassBgLabel = window.findChild(QLabel, "forgotPassBgLabel")
    _forgotPassBgLabel.setPixmap(QPixmap(":img/img/login_page_bg.jpg"))
    _usernameInput = window.findChild(QLineEdit, "usernameInput")
    _emailInput = window.findChild(QLineEdit, "emailInput")
    _sendEmailButton = window.findChild(QPushButton, "sendEmailButton")
    # Set connection
    _sendEmailButton.clicked.connect(lambda: sendEmailButtonClicked(window))


def sendEmailButtonClicked(window):
    # TODO: add notification pane
    # TODO: send email
    print("email sent")
