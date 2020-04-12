from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5 import uic

import resource
from page.login.forgot_password_page import initForgotPasswordPage
from util.mysql_controller import execQuery


def initLoginPage(window):
    global _usernameInput, _passwordInput, _loginButton, _forgotPasswordButton
    # Load ui
    uifile = QFile(":ui/ui/login_page.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, window)
    uifile.close()
    # Get object from ui
    _loginBgLabel = window.findChild(QLabel, "loginBgLabel")
    _loginBgLabel.setPixmap(QPixmap(":img/img/login_page_bg.jpg"))
    _usernameInput = window.findChild(QLineEdit, "usernameInput")
    _passwordInput = window.findChild(QLineEdit, "passwordInput")
    _loginButton = window.findChild(QPushButton, "loginButton")
    _forgotPasswordButton = window.findChild(QPushButton, "forgotPasswordButton")
    # Set connection
    _loginButton.clicked.connect(lambda: loginButtonClicked(window))
    _forgotPasswordButton.clicked.connect(lambda: forgotPasswordButtonClicked(window))


def loginButtonClicked(window):
    global _usernameInput, _passwordInput
    username = _usernameInput.displayText()
    password = _passwordInput.displayText()
    # Check username and password
    if len(username) == 0 or len(password) == 0:
        _passwordInput.setText("Username or password cannot be empty")
        return
    # Query database
    query = "SELECT * FROM user WHERE username='{0}' AND password='{1}'".format(
                    username, password)
    user = execQuery(query)
    if user:
        uifile = QFile(":ui/ui/next_page.ui")
        uifile.open(QFile.ReadOnly)
        uic.loadUi(uifile, window)
        uifile.close()
    # Not found
    _passwordInput.setText("Invalid username or password")


def forgotPasswordButtonClicked(window):
    initForgotPasswordPage(window)
