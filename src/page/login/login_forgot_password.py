from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QLineEdit, QPushButton
from PyQt5 import uic

from util.mysql_controller import execQuery


def setupForgotPasswordContent(content):
    global _usernameInput_L_3, _emailInput_L_3, _sendEmailButton_L_3
    # Get object from ui
    _usernameInput_L_3 = content.findChild(QLineEdit, "usernameInput_L_3")
    _emailInput_L_3 = content.findChild(QLineEdit, "emailInput_L_3")
    _sendEmailButton_L_3 = content.findChild(QPushButton, "sendEmailButton_L_3")
    # Asserting object findChild successful
    assert _usernameInput_L_3 is not None
    assert _emailInput_L_3 is not None
    assert _sendEmailButton_L_3 is not None
    # Set connection
    _sendEmailButton_L_3.clicked.connect(lambda: sendEmailButtonClicked(content))


def sendEmailButtonClicked(content):
    global _usernameInput_L_3, _emailInput_L_3
    username = _usernameInput_L_3.displayText()
    email = _emailInput_L_3.displayText()
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
        _emailInput_L_3.setText("Email sent")
    else:  # Not found
        _emailInput_L_3.setText("Username not found")
