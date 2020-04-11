from PyQt5.QtWidgets import QPushButton, QLineEdit
from PyQt5 import uic

from util.csv_reader import readCSV


def initLoginPage(window):
    global _usernameInput, _passwordInput, _loginButton
    # Load ui
    # TODO: change ui loader to .py file
    uic.loadUi("../ui/login_page.ui", window)
    # Get object from ui
    _usernameInput = window.findChild(QLineEdit, "usernameInput")
    _passwordInput = window.findChild(QLineEdit, "passwordInput")
    _loginButton = window.findChild(QPushButton, "loginButton")
    # Set connection
    _loginButton.clicked.connect(lambda: loginButtonClicked(window))


def loginButtonClicked(window):
    global _usernameInput, _passwordInput
    # Check username and password
    userDB = readCSV("../db/user.csv")
    for id, user in userDB.items():
        if (user["username"] == _usernameInput.displayText()
                and user["password"] == _passwordInput.displayText()):
            uic.loadUi("../ui/login_page2.ui", window)
    # Not found
    _passwordInput.setText("Invalid username or password")
