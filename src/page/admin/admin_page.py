from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5 import uic

import resource
from page.login.forgot_password_page import initForgotPasswordPage
from util.mysql_controller import execQuery

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