import sys
from PyQt5 import QtWidgets

# import etc.populate_db as populate_db
from page.login.login_page import initLoginPage
from page.dosen.dosen_page import initDosenPage


def init():
    global window, button, textEdit
    # Create app
    app = QtWidgets.QApplication(sys.argv)
    # Create and show window
    window = QtWidgets.QMainWindow()
    initDosenPage(window, None)
    window.show()
    # Exec app
    app.exec_()


if __name__ == '__main__':
    # populate_db.populate()
    init()
