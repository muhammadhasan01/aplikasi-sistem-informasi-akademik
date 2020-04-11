from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5 import uic

import resource
from util.csv_reader import readCSV
from page.login.forgot_password_page import initForgotPasswordPage


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
    # Check username and password
    userDB = readCSV("db/user.csv")
    for id, user in userDB.items():
        if (user["username"] == _usernameInput.displayText()
                and user["password"] == _passwordInput.displayText()):
            uifile = QFile(":ui/ui/next_page.ui")
            uifile.open(QFile.ReadOnly)
            uic.loadUi(uifile, window)
            uifile.close()
    # Not found
    _passwordInput.setText("Invalid username or password")


def forgotPasswordButtonClicked(window):
    initForgotPasswordPage(window)
