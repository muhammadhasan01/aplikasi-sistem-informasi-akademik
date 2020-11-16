from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5 import uic

import resource
from page.login.login_login import setupLoginContent
from page.login.login_forgot_password import setupForgotPasswordContent


def initLoginPage(window):
    global _contentLogin_L_1, _contentForgotPassword_L_1, _mainVLayout_L_1
    # Load layout ui
    uifile = QFile(":ui/ui/login_layout.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, window)
    uifile.close()
    # Get objeck from layout ui
    _loginBgLabel_L_1 = window.findChild(QLabel, "loginBgLabel_L_1")
    _mainVLayout_L_1 = window.findChild(QVBoxLayout, "mainVLayout_L_1")
    # Asserting object findChild successful
    assert _loginBgLabel_L_1 is not None
    # Set background
    _loginBgLabel_L_1.setPixmap(QPixmap(":img/img/login_page_bg.jpg"))

    # Create and load content login widget
    _contentLogin_L_1 = QWidget()
    uifile = QFile(":ui/ui/login_login.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, _contentLogin_L_1)
    uifile.close()
    setupLoginContent(window, _contentLogin_L_1)
    # Get forget password button and set connection
    _forgotPasswordButton_L_2 = _contentLogin_L_1.findChild(QPushButton, "forgotPasswordButton_L_2")
    assert _forgotPasswordButton_L_2 is not None
    _forgotPasswordButton_L_2.clicked.connect(lambda: forgotPasswordButtonClicked())

    # Create and load content dashboard widget
    _contentForgotPassword_L_1 = QWidget()
    uifile = QFile(":ui/ui/login_forgot_password.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, _contentForgotPassword_L_1)
    uifile.close()
    setupForgotPasswordContent(_contentForgotPassword_L_1)
    # Get login page button and set connection
    _loginPageButton_L_3 = _contentForgotPassword_L_1.findChild(QPushButton, "loginPageButton_L_3")
    assert _loginPageButton_L_3 is not None
    _loginPageButton_L_3.clicked.connect(lambda: loginPageButtonClicked())

    # Set widgets to layout
    _mainVLayout_L_1.addWidget(_contentLogin_L_1)
    _mainVLayout_L_1.addWidget(_contentForgotPassword_L_1)

    # Simulate login page button click
    loginPageButtonClicked()


def loginPageButtonClicked():
    global _contentLogin_L_1, _contentForgotPassword_L_1
    # Set visible content
    _contentLogin_L_1.setVisible(True)
    _contentForgotPassword_L_1.setVisible(False)


def forgotPasswordButtonClicked():
    global _contentLogin_L_1, _contentForgotPassword_L_1
    # Set visible content
    _contentLogin_L_1.setVisible(False)
    _contentForgotPassword_L_1.setVisible(True)
