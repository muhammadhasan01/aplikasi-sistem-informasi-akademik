from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget
from PyQt5 import uic

import resource
from page.admin.admin_navbar import getNavBarAdmin
from page.admin.admin_setup_user import setupUserContent
from page.admin.admin_setup_matkul import setupMatkulContent


def initAdminPage(window, auth):
  global _navbar_A, _content_A_dashboard, _content_A_1, _content_A_2, _mainVLayout_A
  # Load ui
  uifile = QFile(":ui/ui/admin/admin_layout.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, window)
  uifile.close()  # Get object from layout ui
  _mainVLayout_A = window.findChild(QVBoxLayout, "mainVLayout_A")

  #load navbar widget
  _navbar_A = QWidget()
  uifile = QFile(":ui/ui/admin/admin_navbar.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, _navbar_A)
  uifile.close()
  
  #set up logo
  _logoSiak_A = _navbar_A.findChild(QLabel, "logoSiak")
  _logoSiak_A.setPixmap(QPixmap(":img/img/logo_siak_full.png"))
  
  
  #load content
  _content_A_dashboard = QWidget()
  uifile = QFile(":ui/ui/admin/admin_content_dashboard.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, _content_A_dashboard)
  uifile.close()

  _content_A_1 = QWidget()
  uifile = QFile(":ui/ui/admin/admin_content_user.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, _content_A_1)
  uifile.close()
  _content_A_1.setVisible(False)

  _content_A_2 = QWidget()
  uifile = QFile(":ui/ui/admin/admin_content_matkul.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, _content_A_2)
  uifile.close()
  _content_A_2.setVisible(False)


  #set admin name to auth and image to default
  _adminName_A_1 = _content_A_dashboard.findChild(QLabel, "adminName")
  _adminImage_A_1 = _content_A_dashboard.findChild(QLabel, "adminImage")
  _adminName_A_1.setText(auth.username)
  pixmap = QPixmap(":img/img/profil_default.png")
  pixmap = pixmap.scaledToHeight(300)
  _adminImage_A_1.setPixmap(pixmap)

  #Load widgets to layout
  _mainVLayout_A.addWidget(_navbar_A)
  _mainVLayout_A.addWidget(_content_A_dashboard)
  _mainVLayout_A.addWidget(_content_A_1)
  _mainVLayout_A.addWidget(_content_A_2)
  _navbar_A.setFixedHeight(200)

  #set up buttons
  _berandaButton_A = _navbar_A.findChild(QPushButton, "berandaButton")
  _userButton_A = _navbar_A.findChild(QPushButton, "userButton")
  _matkulButton_A = _navbar_A.findChild(QPushButton, "matkulButton")
  _berandaButton_A.clicked.connect(lambda: berandaButtonClicked())
  _userButton_A.clicked.connect(lambda: userButtonClicked())
  _matkulButton_A.clicked.connect(lambda: matkulButtonClicked())


def berandaButtonClicked():
  global _content_A_dashboard, _content_A_1, _content_A_2, _mainVLayout_A
  _content_A_1.setVisible(False)
  _content_A_2.setVisible(False)
  _content_A_dashboard.setVisible(True)

def userButtonClicked():
  _content_A_1.setVisible(True)
  _content_A_2.setVisible(False)
  _content_A_dashboard.setVisible(False)

  setupUserContent(_content_A_1)

def matkulButtonClicked():
  _content_A_1.setVisible(False)
  _content_A_2.setVisible(True)
  _content_A_dashboard.setVisible(False)

  setupMatkulContent(_content_A_2)

# import resource
# from page.login.forgot_password_page import initForgotPasswordPage
# from util.mysql_controller import execQuery

#def initAdminPage(window):

#toHomePage()
#   homeButton_A_30
#       change address to home page
#       does nothing if already in home page
#
#def homeButton_A_30():

#toUserPage()
#   userButton_A_30
#       get data from user_table
#       display as user_list
#
#def userButton_A_30():

#toMatkulPage
#   matkulButton_A_30
#       get data from matkul_table
#       display as matkul_list
#
#def matkulButton_A_30():

#sortUserBy(string)
#   sort_user_byButton_A_30
#       sort user_table as per preset string conditions
#       display as user_list
#
#def sort_user_byButton_A_30():

#addUser()
#   add_userButton_A_30
#       adds user to user_table
#       display as user_list
#
#def add_userButton_A_30():

#updateUser()
#   update_userButton_A_30
#       change user data in user_table
#       display as user_list
#   #repeated across all tuples
#
#def update_userButton_A_30():

#removeUser()
#   remove_UserButton_A_30
#       remove user tuple from user_table
#       display as user_list
#   #repeated across all tuples
#
#def remove_userButton_A_30():

#sortMatkulBy(string)
#   sort_matkul_byButton_A_31
#       sort matkul_table as per preset string conditions
#       display as matkul_list
#
#def sort_matkul_byButton_A_31():

#addMatkul()
#   add_matkulButton_A_31
#       add matkul to matkul_table
#       display as matkul_list
#
#def add_matkulButton_A_31():

#updateMatkul()
#   update_matkul_A_31
#       change a matkul data in matkul_table
#       display as matkul_list
#   #repeated across all tuples
#
#def update_matkul_A_31():

#removeMatkul()
#   remove_matkul_A_31
#       remove matkul tuple from matkul_table
#       display as matkul_list
#   #repeated across all tuples
#
#def remove_matkul_A_31():

#display user_list
#
#def display_user_list():

#display matkul_list
#
#def display_matkul_list():
