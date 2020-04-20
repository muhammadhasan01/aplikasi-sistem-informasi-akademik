from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QLineEdit, QPushButton, QMessageBox
from PyQt5 import uic

from page.dosen.dosen_page import initDosenPage
from page.mahasiswa.mahasiswa_page import initMahasiswaPage
from page.admin.admin_page import initAdminPage
from util.mysql_controller import execQuery


def setupLoginContent(window, content):
    global _usernameInput_L_2, _passwordInput_L_2
    # Get object from ui
    _usernameInput_L_2 = content.findChild(QLineEdit, "usernameInput_L_2")
    _passwordInput_L_2 = content.findChild(QLineEdit, "passwordInput_L_2")
    _loginButton_L_2 = content.findChild(QPushButton, "loginButton_L_2")
    # Asserting object findChild successful
    assert _usernameInput_L_2 is not None
    assert _passwordInput_L_2 is not None
    assert _loginButton_L_2 is not None
    # Mask password
    _passwordInput_L_2.setEchoMode(QLineEdit.Password)

    # Set connection
    _usernameInput_L_2.returnPressed.connect(lambda: loginButtonClicked(window))
    _passwordInput_L_2.returnPressed.connect(lambda: loginButtonClicked(window))
    _loginButton_L_2.clicked.connect(lambda: loginButtonClicked(window))


def loginButtonClicked(window):
    global _usernameInput_L_2, _passwordInput_L_2
    message = QMessageBox()
    message.setIcon(QMessageBox.Information)
    message.setWindowTitle("Invalid login")
    # Get text
    username = _usernameInput_L_2.text()
    password = _passwordInput_L_2.text()
    # Check username and password
    if len(username) == 0 or len(password) == 0:
        message.setText("Username or password cannot be empty")
        message.exec_()
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
        elif (user[0].role == "mahasiswa"):
            initMahasiswaPage(window, user[0])
        else:
            initAdminPage(window,user[0])
    else:  # Not found
        message.setText("Invalid username or password")
        message.exec_()
