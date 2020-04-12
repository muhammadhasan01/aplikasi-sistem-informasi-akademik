from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5 import uic

import resource
from page.login.forgot_password_page import initForgotPasswordPage
from util.mysql_controller import execQuery

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

#def berandaButtonClicked():
#   homeButton_A_30
#       change address to home page
#       does nothing if already in home page

#def userButtonClicked():
#   userButton_A_30
#       get data from user_table
#       display as user_list

#def matkulButtonClicked():
#   matkulButton_A_30
#       get data from matkul_table
#       display as matkul_list

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

#def display_user_list(window):
#

#def display_matkul_list(window):
#