from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QLineEdit, QPushButton
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

    # Set connection
    _loginButton_L_2.clicked.connect(lambda: loginButtonClicked(window))


def loginButtonClicked(window):
    global _usernameInput_L_2, _passwordInput_L_2
    username = _usernameInput_L_2.displayText()
    password = _passwordInput_L_2.displayText()
    # Check username and password
    if len(username) == 0 or len(password) == 0:
        _passwordInput_L_2.setText("Username or password cannot be empty")
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
        _passwordInput_L_2.setText("Invalid username or password")
