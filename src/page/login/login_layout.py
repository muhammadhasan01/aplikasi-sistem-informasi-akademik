from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

import resource
from page.login.login_login import setupLoginContent
from page.login.login_forgot_password import setupForgotPasswordContent


def initLoginPage(window):
    global _content_L_1
    # Load layout ui
    uifile = QFile(":ui/ui/new_login_layout.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, window)
    uifile.close()
    # Get objeck from layout ui
    _loginBgLabel_L_1 = window.findChild(QLabel, "loginBgLabel_L_1")
    # Asserting object findChild successful
    assert _loginBgLabel_L_1 is not None
    # Set background
    _loginBgLabel_L_1.setPixmap(QPixmap(":img/img/login_page_bg.jpg"))

    # Create and load content dashboard widget
    _content_L_1 = QWidget()
    uifile = QFile(":ui/ui/new_login_login.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, _content_L_1)
    uifile.close()
    # setupLogin
    loginPageButtonClicked(window)

    # Set widgets to layout
    window.addWidget(_content_L_1)


def loginPageButtonClicked(window):
    global _content_L_1
    # Create new widget
    newWidget = QWidget()
    uifile = QFile(":ui/ui/new_login_login.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, newWidget)
    uifile.close()
    setupLoginContent(newWidget)
    # Set up the new widget
    window.removeWidget(_content_L_1)
    _content_L_1 = newWidget
    window.addWidget(_content_L_1)

    # Get forget password button and set connection
    _forgotPasswordButton_L_3 = _content_L_1.findChild(QPushButton, "forgotPasswordButton_L_3")
    assert _forgotPasswordButton_L_3 is not None
    _forgotPasswordButton_L_3.clicked.connect(lambda: forgotPasswordButtonClicked(window))


def forgotPasswordButtonClicked(window):
    global _content_L_1
    # Create new widget
    newWidget = QWidget()
    uifile = QFile(":ui/ui/new_login_login.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, newWidget)
    uifile.close()
    setupForgotPasswordContent(newWidget)
    # Set up the new widget
    window.removeWidget(_content_L_1)
    _content_L_1 = newWidget
    window.addWidget(_content_L_1)

    # Get forget password button and set connection
    _loginPageButton_L_2 = _content_L_1.findChild(QPushButton, "loginPageButton_L_2")
    assert _loginPageButton_L_2 is not None
    _loginPageButton_L_2.clicked.connect(lambda: loginPageButtonClicked(window))
