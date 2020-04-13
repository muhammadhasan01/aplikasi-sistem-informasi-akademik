from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QPushButton
from PyQt5.QtCore import QFile, Qt
from PyQt5 import uic

from util.mysql_controller import execQuery

def setupUserContent(content):
    global _userVLayout_A_1
    _userVLayout_A_1 = content.findChild(QVBoxLayout, "userVLayout")
    # Assert that the query successful
    assert _userVLayout_A_1 is not None

    _userVLayout_A_1.setAlignment(Qt.AlignTop)
    _userA = QVBoxLayout()
    

    button = QPushButton()
    test = QHBoxLayout()
    test.addWidget(button)
    setUpUserLayout(_userVLayout_A_1)

    #format row : id; username; password; role; image
    user = getUsers()

def setUpUserLayout(layout:QVBoxLayout):
  listOfUserBox = list()
  hBox = QHBoxLayout()
  userBox = QGroupBox()
  userBox.setLayout(hBox)
  uifile = QFile(":ui/ui/admin/admin_user_box.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, userBox)
  uifile.close()
  layout.addWidget(userBox)

def getUsers():
  query = """SELECT * FROM user"""
  users = execQuery(query)
  return users
