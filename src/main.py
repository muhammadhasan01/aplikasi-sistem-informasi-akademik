import sys
from PyQt5 import QtWidgets

# import etc.populate_db as populate_db
from page.login.login_page import initLoginPage
from util.test_login import test_login

def init():
    global window, button, textEdit
    # Create app
    app = QtWidgets.QApplication(sys.argv)
    # Create and show window
    window = QtWidgets.QMainWindow()
    initLoginPage(window)
    window.show()
    # Exec app
    app.exec_()


if __name__ == '__main__':
    # populate_db.populate()
    init()
