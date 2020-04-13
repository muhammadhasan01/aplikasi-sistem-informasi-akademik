from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QPushButton, QMessageBox
from PyQt5.QtCore import QFile, Qt
from PyQt5 import uic

from util.mysql_controller import execQuery

def setupUserContent(content):
    global _userVLayout_A_1
    _userVLayout_A_1 = content.findChild(QVBoxLayout, "userVLayout")
    _addUser_A_1 = content.findChild(QPushButton, "addUser")

    # Assert that the query successful
    assert _userVLayout_A_1 is not None

    _userVLayout_A_1.setAlignment(Qt.AlignTop)
    _userA = QVBoxLayout()
    
    listOfUsers = getUsers()

    for i in range(listOfUsers.__len__()):
      userBox = QGroupBox()
      uifile = QFile(":ui/ui/admin/admin_user_box.ui")
      uifile.open(QFile.ReadOnly)
      uic.loadUi(uifile, userBox)
      uifile.close()
      userBox.setFixedHeight(50)
      setUserBoxData(userBox, listOfUsers.__getitem__(i))
      _userVLayout_A_1.addWidget(userBox)
    
    #set button onclick
    _addUser_A_1.clicked.connect(lambda: showAddUserPopUp())


def setUserBoxData(userBox:QGroupBox, user):
  userName = userBox.findChild(QLabel, "userName")
  userPassword = userBox.findChild(QLabel, "userPassword")
  userType = userBox.findChild(QLabel, "userType")
  #format row : id; username; password; role; image
  userName.setText(user.username)
  userPassword.setText(user.password)
  userType.setText(user.role)
  userName.setAlignment(Qt.AlignCenter)
  userPassword.setAlignment(Qt.AlignCenter)
  userType.setAlignment(Qt.AlignCenter)

def showAddUserPopUp():
  addUserPopup = QWidget()
  addUserPopup.setFixedHeight(500)
  addUserPopup.setFixedWidth(500)

def getUsers():
  query = """SELECT * FROM user"""
  users = execQuery(query)
  return users
