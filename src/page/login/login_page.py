from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5 import uic

import resource
from page.login.forgot_password_page import initForgotPasswordPage
from page.dosen.dosen_page import initDosenPage
from util.mysql_controller import execQuery


def initLoginPage(window):
    global _usernameInput_L_1, _passwordInput_L_1, _loginButton_L_1, _forgotPasswordButton_L_1
    # Load ui
    uifile = QFile(":ui/ui/login_page.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, window)
    uifile.close()
    # Get object from ui
    _loginBgLabel_L_1 = window.findChild(QLabel, "loginBgLabel_L_1")
    _usernameInput_L_1 = window.findChild(QLineEdit, "usernameInput_L_1")
    _passwordInput_L_1 = window.findChild(QLineEdit, "passwordInput_L_1")
    _loginButton_L_1 = window.findChild(QPushButton, "loginButton_L_1")
    _forgotPasswordButton_L_1 = window.findChild(QPushButton, "forgotPasswordButton_L_1")
    # Asserting object findChild successful
    assert _loginBgLabel_L_1 is not None
    assert _usernameInput_L_1 is not None
    assert _passwordInput_L_1 is not None
    assert _loginButton_L_1 is not None
    assert _forgotPasswordButton_L_1 is not None
    # Set background
    _loginBgLabel_L_1.setPixmap(QPixmap(":img/img/login_page_bg.jpg"))
    # Set connection
    _loginButton_L_1.clicked.connect(lambda: loginButtonClicked(window))
    _forgotPasswordButton_L_1.clicked.connect(lambda: forgotPasswordButtonClicked(window))


def loginButtonClicked(window):
    global _usernameInput_L_1, _passwordInput_L_1
    username = _usernameInput_L_1.displayText()
    password = _passwordInput_L_1.displayText()
    # Check username and password
    if len(username) == 0 or len(password) == 0:
        _passwordInput_L_1.setText("Username or password cannot be empty")
        return
    # Query database
    query = "SELECT * FROM user WHERE username=%s AND password=%s"
    format = (username, password,)
    user = None
    try:
        user = execQuery(query, format)
    except Exception as e:
        print(e)
    # Cek if user found
    if user:
        if (user[0].role == "dosen"):
            initDosenPage(window, user[0])
        else:
            uifile = QFile(":ui/ui/next_page.ui")
            uifile.open(QFile.ReadOnly)
            uic.loadUi(uifile, window)
            uifile.close()
    else:  # Not found
        _passwordInput_L_1.setText("Invalid username or password")


def forgotPasswordButtonClicked(window):
    initForgotPasswordPage(window)
