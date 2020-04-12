import sys
from PyQt5 import QtWidgets

# import etc.populate_db as populate_db
from page.login.login_page import initLoginPage
from page.admin.admin_page import initAdminPage

def init():
    global window, button, textEdit
    # Create app
    app = QtWidgets.QApplication(sys.argv)
    # Create and show window
    window = QtWidgets.QMainWindow()
    initAdminPage(window,"huahuahua")
    # initLoginPage(window)
    window.show()
    # Exec app
    app.exec_()


if __name__ == '__main__':
    # populate_db.populate()
    init()
