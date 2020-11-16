from PyQt5.QtWidgets import QLineEdit, QPushButton, QMessageBox

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
    _usernameInput_L_3.returnPressed.connect(lambda: sendEmailButtonClicked(content))
    _emailInput_L_3.returnPressed.connect(lambda: sendEmailButtonClicked(content))
    _sendEmailButton_L_3.clicked.connect(lambda: sendEmailButtonClicked(content))


def sendEmailButtonClicked(content):
    global _usernameInput_L_3, _emailInput_L_3
    message = QMessageBox()
    message.setIcon(QMessageBox.Information)
    message.setWindowTitle("Invalid input")
    # Get text
    username = _usernameInput_L_3.text()
    email = _emailInput_L_3.text()
    # Check username and password
    if len(username) == 0 or len(email) == 0:
        message.setText("Username or email cannot be empty")
        message.exec_()
        return
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
        message.setText("Email sent")
        message.exec_()
    else:  # Not found
        message.setText("Username not found")
        message.exec_()
