from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5 import uic

import resource
from util.mysql_controller import execQuery


def initForgotPasswordPage(window):
    global _usernameInput_L_2, _emailInput_L_2, _sendEmailButton_L_2
    # Load ui
    uifile = QFile(":ui/ui/forgot_password_page.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, window)
    uifile.close()
    # Get object from ui
    _loginBgLabel_L_2 = window.findChild(QLabel, "loginBgLabel_L_2")
    _usernameInput_L_2 = window.findChild(QLineEdit, "usernameInput_L_2")
    _emailInput_L_2 = window.findChild(QLineEdit, "emailInput_L_2")
    _sendEmailButton_L_2 = window.findChild(QPushButton, "sendEmailButton_L_2")
    # Asserting object findChild successful
    assert _loginBgLabel_L_2 is not None
    assert _usernameInput_L_2 is not None
    assert _emailInput_L_2 is not None
    assert _sendEmailButton_L_2 is not None
    # Set background
    _loginBgLabel_L_2.setPixmap(QPixmap(":img/img/login_page_bg.jpg"))
    # Set connection
    _sendEmailButton_L_2.clicked.connect(lambda: sendEmailButtonClicked(window))


def sendEmailButtonClicked(window):
    global _usernameInput_L_2, _emailInput_L_2
    username = _usernameInput_L_2.displayText()
    email = _emailInput_L_2.displayText()
    # TODO: add notification pane
    # Query database
    query = "SELECT * FROM user WHERE username=%s"
    format = (username,)
    user = None
    try:
        user = execQuery(query, format)
    except Exception as e:
        print(e)
    # Cek if user found
    if user:
        print(f"""\
Email sent to : {email}
Content       :
  username = {user[0].username}
  password = {user[0].password}\
""")
        _emailInput_L_2.setText("Email sent")
    else: # Not found
        _emailInput_L_2.setText("Username not found")
