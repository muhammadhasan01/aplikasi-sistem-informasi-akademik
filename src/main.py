import sys
from PyQt5 import QtWidgets

from page.login.login_page import initLoginPage


def init():
    global window, button, textEdit
    # Create app
    app = QtWidgets.QApplication(sys.argv)
    # Create and show window
    window = QtWidgets.QMainWindow()
    # initLoginPage(window)
    window.show()
    # Exec app
    app.exec_()


if __name__ == '__main__':
    init()
