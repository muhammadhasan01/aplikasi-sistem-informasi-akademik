from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget
from PyQt5 import uic

import resource
from page.admin.admin_navbar import getNavBarAdmin


def initAdminPage(window, auth):
  global _navbar_A, _content_A, _mainVLayout_A
  # Load ui
  uifile = QFile(":ui/ui/admin/admin_layout.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, window)
  uifile.close()
  # Get object from layout ui
  _mainVLayout_A = window.findChild(QVBoxLayout, "mainVLayout_A")

  #load navbar widget
  _navbar_A = getNavBarAdmin()
  
  #load content
  _content_A = QWidget()
  uifile = QFile(":ui/ui/admin/admin_content_dashboard.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, _content_A)
  uifile.close()

  #set admin name to auth and image to default
  _adminName_A_1 = _content_A.findChild(QLabel, "adminName")
  _adminImage_A_1 = _content_A.findChild(QLabel, "adminImage")
  _adminName_A_1.setText(auth)
  pixmap = QPixmap(":img/img/profil_default.png")
  pixmap = pixmap.scaledToHeight(300)
  _adminImage_A_1.setPixmap(pixmap)

  #Load widgets to layout
  _mainVLayout_A.addWidget(_navbar_A)
  _mainVLayout_A.addWidget(_content_A)
  _navbar_A.setFixedHeight(200)

  #set up buttons
  _berandaButton_A = _navbar_A.findChild(QPushButton, "berandaButton")
  _userButton_A = _navbar_A.findChild(QPushButton, "userButton")
  _matkulButton_A = _navbar_A.findChild(QPushButton, "matkulButton")
  _berandaButton_A.clicked.connect(lambda: berandaButtonClicked())
  _userButton_A.clicked.connect(lambda: userButtonClicked())
  _matkulButton_A.clicked.connect(lambda: matkulButtonClicked())

def berandaButtonClicked():
  global _content_A, _mainVLayout_A
  newWidget = QWidget()
  uifile = QFile(":ui/ui/admin/admin_content_dashboard.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, newWidget)
  uifile.close()
  _mainVLayout_A.removeWidget(_content_A)
  _content_A = newWidget
  _mainVLayout_A.addWidget(_content_A)

def userButtonClicked():
  global _content_A, mainVLayout_A
  newWidget = QWidget()
  uifile = QFile(":ui/ui/admin/admin_content_user.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, newWidget)
  uifile.close()
  _mainVLayout_A.removeWidget(_content_A)
  _content_A = newWidget
  _mainVLayout_A.addWidget(_content_A)

def matkulButtonClicked():
  global _content_A, mainVLayout_A
  newWidget = QWidget()
  uifile = QFile(":ui/ui/admin/admin_content_matkul.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, newWidget)
  uifile.close()
  _mainVLayout_A.removeWidget(_content_A)
  _content_A = newWidget
  _mainVLayout_A.addWidget(_content_A)

# import resource
# from page.login.forgot_password_page import initForgotPasswordPage
# from util.mysql_controller import execQuery

#def initAdminPage(window):
    #global _homeButton_A_30, _userButton_A_30, _matkulButton_A_30, _sort_user_byButton_A_30, _add_userButton_A_30, _update_userButton_A_30, _remove_userButton_A_30, _sort_matkul_byButton_A_31, _add_matkulButton_A_31, _update_matkulButton_A_31, _remove_matkulButton_A_31
    #Load ui
    #uifile = QFile("") #add filename
    #uifile.open(QFile.ReadOnly)
    #uic.loadUi(uifile, window)
    #uifile.close()
    #Get object from ui
    #_homeButton_A_30 = window.findChild(QPushButton, "homeButton_A_30")
    #_userButton_A_30 = window.findChild(QPushButton, "userButton_A_30")
    #_matkulButton_A_30 = window.findChild(QPushButton, "matkulButton_A_30")
    #_sort_user_byButton_A_30 = window.findChild(QPushButton, "sort_user_byButton_A_30")
    #_add_userButton_A_30 = window.findChild(QPushButton, "add_userButton_A_30")
    #_update_userButton_A_30 = window.findChild(QPushButton, "update_userButton_A_30")
    #_remove_userButton_A_30 = window.findChild(QPushButton, "remove_userButton_A_30")
    #_sort_matkul_byButton_A_31 = window.findChild(QPushButton, "sort_matkul_byButton_A_31")
    #_add_matkulButton_A_31 = window.findChild(QPushButton, "add_matkulButton_A_31")
    #_update_matkulButton_A_31 = window.findChild(QPushButton, "update_matkulButton_A_31")
    #_remove_matkulButton_A_31 = window.findChild(QPushButton, "remove_matkulButton_A_31")
    # Asserting object findChild successful
    #assert _homeButton_A_30 is not None
    #assert _userButton_A_30 is not None
    #assert _matkulButton_A_30 is not None
    #assert _sort_user_byButton_A_30 is not None
    #assert _add_userButton_A_30 is not None
    #assert _update_userButton_A_30 is not None
    #assert _remove_userButton_A_30 is not None
    #assert _sort_matkul_byButton_A_31 is not None
    #assert _add_matkulButton_A_31 is not None
    #assert _update_matkulButton_A_31 is not None
    #assert _remove_matkulButton_A_31 is not None

    # Set background
    # Set connection

#def sortUserBy(string):
#   sort_user_byButton_A_30
#       sort user_table as per preset string conditions
#       display as user_list

#def addUserButtonClicked():
#   add_userButton_A_30
#       adds user to user_table
#       display as user_list

#def updateUserButtonClicked():
#   update_userButton_A_30
#       change user data in user_table
#       display as user_list
#   #repeated across all tuples

#def removeUserButtonClicked():
#   remove_UserButton_A_30
#       remove user tuple from user_table
#       display as user_list
#   #repeated across all tuples

#def sortMatkulByButtonClicked(string):
#   sort_matkul_byButton_A_31
#       sort matkul_table as per preset string conditions
#       display as matkul_list

#def addMatkulButtonClicked():
#   add_matkulButton_A_31
#       add matkul to matkul_table
#       display as matkul_list

#def updateMatkulButtonClicked():
#   update_matkul_A_31
#       change a matkul data in matkul_table
#       display as matkul_list
#   #repeated across all tuples

#def removeMatkulButtonClicked():
#   remove_matkul_A_31
#       remove matkul tuple from matkul_table
#       display as matkul_list
#   #repeated across all tuples
