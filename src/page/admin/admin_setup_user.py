from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QPushButton, QTextEdit
from PyQt5.QtCore import QFile, Qt
from PyQt5 import uic

from util.mysql_controller import execQuery

def setupUserContent(content):
    global _userVLayout_A_1, _content_A_1
    _content_A_1 = content
    _userVLayout_A_1 = content.findChild(QVBoxLayout, "userVLayout")
    _addUser_A_1 = content.findChild(QPushButton, "addUser")

    for i in reversed(range(_userVLayout_A_1.count())): 
      _userVLayout_A_1.itemAt(i).widget().setParent(None)
    
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
      user = listOfUsers.__getitem__(i)
      setUserBoxData(userBox, user)
      _userVLayout_A_1.addWidget(userBox)
      _removeUser_A_1 = userBox.findChild(QPushButton,"removeUser")
      _removeUser_A_1.clicked.connect(lambda: removeUser(user.id))
    
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
  global _addUserPopup_A_1
  _addUserPopup_A_1 = QWidget()
  uifile = QFile(":ui/ui/admin/admin_content_user_add_user.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, _addUserPopup_A_1)
  uifile.close()

  _addUserPopup_A_1.setFixedHeight(645)
  _addUserPopup_A_1.setFixedWidth(1000)

  _submit_form_A_1 = _addUserPopup_A_1.findChild(QPushButton, "submitButton")
  _submit_form_A_1.clicked.connect(lambda:insertUserToDatabaseAndRenderPage())
  _addUserPopup_A_1.show()

def removeUser(userId):
  query = "DELETE FROM user WHERE id = %s"
  format = (userId,)
  execQuery(query,format=format,queryType="DELETE")


def insertUserToDatabaseAndRenderPage():
  global _addUserPopup_A_1, _content_A_1
  _userUsername = _addUserPopup_A_1.findChild(QTextEdit, "userUsername")
  _userPassword = _addUserPopup_A_1.findChild(QTextEdit, "userPassword")
  _userRole = _addUserPopup_A_1.findChild(QTextEdit, "userRole")
  _userImage = _addUserPopup_A_1.findChild(QTextEdit, "userImage")

  userUserName = _userUsername.toPlainText()
  userPassword = _userPassword.toPlainText()
  userRole = _userRole.toPlainText()
  userImage = _userImage.toPlainText()

  query = 'INSERT INTO user(username,password,role,image) values(%s,%s,%s,%s)'
  format = (userUserName, userPassword, userRole, userImage) 
  execQuery(query,format=format,queryType="INSERT")
  setupUserContent(_content_A_1)

def getUsers():
  query = """SELECT * FROM user"""
  users = execQuery(query)
  return users
