import sys
from PyQt5 import QtWidgets

import etc.populate_db as populate_db
import page.login_page as login_page


def init():
    global window, button, textEdit
    # Create app
    app = QtWidgets.QApplication(sys.argv)
    # Create and show window
    window = QtWidgets.QMainWindow()
    login_page.initLoginPage(window)
    window.show()
    # Exec app
    app.exec_()


if __name__ == '__main__':
    # populate_db.populate()
    init()
