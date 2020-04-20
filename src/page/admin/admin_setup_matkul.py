from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QPushButton, QTextEdit
from PyQt5.QtCore import QFile, Qt
from PyQt5 import uic

from util.mysql_controller import execQuery

import datetime
"""
  datetime is used for extracting the jadwal info from mysql, because python treats sql date as
  datetime.timedelta, so we need to import this in order to use its tostring method
"""

_jadwal_A_2 = None

def setupMatkulContent(content):
    global _matkulVLayout_A_2, _content_A_2, _jadwal_A_2
    _jadwal_A_2 = getJadwals()
    _content_A_2 = content
    _matkulVLayout_A_2 = content.findChild(QVBoxLayout, "matkulVLayout")
    _addMatkul_A_2 = content.findChild(QPushButton, "addMatkul")

    for i in reversed(range(_matkulVLayout_A_2.count())):
      _matkulVLayout_A_2.itemAt(i).widget().setParent(None)
    
    # Assert that the query successful
    assert _jadwal_A_2 is not None
    assert _content_A_2 is not None
    assert _matkulVLayout_A_2 is not None
    assert _addMatkul_A_2 is not None

    _matkulVLayout_A_2.setAlignment(Qt.AlignTop)
    _matkulA = QVBoxLayout()
    
    listOfMatkul = getMatkuls()

    for i in range(listOfMatkul.__len__()):
      # set up the matkul box
      matkulBox = QGroupBox()
      uifile = QFile(":ui/ui/admin/admin_matkul_box.ui")
      uifile.open(QFile.ReadOnly)
      uic.loadUi(uifile, matkulBox)
      uifile.close()

      matkulBox.setMinimumHeight(50)
      matkul = listOfMatkul.__getitem__(i)
      setMatkulBoxData(matkulBox, matkul)
      _matkulVLayout_A_2.addWidget(matkulBox)
      # _removeUser_A_1 = matkulBox.findChild(QPushButton,"removeUser")
      # _removeUser_A_1.clicked.connect(lambda: removeUser(matkul.id))
    
#     #set button onclick
#     _addMatkul_A_2.clicked.connect(lambda: showAddUserPopUp())

def setMatkulBoxData(userBox:QGroupBox, matkul):
  matkulName : QLabel         = userBox.findChild(QLabel, "matkulName")
  matkulId : QLabel           = userBox.findChild(QLabel, "matkulId")
  matkulJadwal : QLabel       = userBox.findChild(QLabel, "matkulJadwal")
  removeButton : QPushButton  = userBox.findChild(QPushButton, "matkulRemove")
  updateButton :QPushButton   = userBox.findChild(QPushButton, "matkulUpdate")

  matkulJadwal.setFixedWidth(429)
  matkulJadwal.setWordWrap(True)
  jadwal = getJadwalOfMatkul(matkul.kode_matkul)
  jadwalString = ""
  for i in range(jadwal.__len__()):
    #misal ada banyak timeslot, tambahin koma dulu di belakangnya
    if(i > 0):
      jadwalString = jadwalString.__add__(" , ")
    waktu = jadwal[i]
    hari = waktu[0]
    waktuMulai = waktu[1]
    waktuSelesai = waktu[2]
    jadwalString = jadwalString.__add__(str(hari).capitalize() + " " + str(waktuMulai) + " - " + str(waktuSelesai))
  
  #format row : id; username; password; role; image
  matkulName.setText(matkul.nama_matkul)
  matkulId.setText(matkul.kode_matkul)
  matkulJadwal.setText(jadwalString)
  matkulName.setAlignment(Qt.AlignCenter)
  matkulId.setAlignment(Qt.AlignCenter)
  matkulJadwal.setAlignment(Qt.AlignCenter)

  removeButton.clicked.connect(lambda : removeMatkul(matkul.kode_matkul))
  # updateButton.clicked.connect(lambda : showUpdatePopup())


# def showAddUserPopUp():
#   global _addUserPopup_A_1
#   _addUserPopup_A_1 = QWidget()
#   uifile = QFile(":ui/ui/admin/admin_content_user_add_user.ui")
#   uifile.open(QFile.ReadOnly)
#   uic.loadUi(uifile, _addUserPopup_A_1)
#   uifile.close()

#   _addUserPopup_A_1.setFixedHeight(645)
#   _addUserPopup_A_1.setFixedWidth(1000)

#   _submit_form_A_1 = _addUserPopup_A_1.findChild(QPushButton, "submitButton")
#   _submit_form_A_1.clicked.connect(lambda:insertUserToDatabaseAndRenderPage())
#   _addUserPopup_A_1.show()

def removeMatkul(matkulId):
  query = "DELETE FROM mata_kuliah WHERE kode_matkul = %s"
  format = (matkulId,)
  execQuery(query,format=format,queryType="DELETE")


# def insertUserToDatabaseAndRenderPage():
#   global _addUserPopup_A_1, _content_A_1
#   _userUsername = _addUserPopup_A_1.findChild(QTextEdit, "userUsername")
#   _userPassword = _addUserPopup_A_1.findChild(QTextEdit, "userPassword")
#   _userRole = _addUserPopup_A_1.findChild(QTextEdit, "userRole")
#   _userImage = _addUserPopup_A_1.findChild(QTextEdit, "userImage")

#   userUserName = _userUsername.toPlainText()
#   userPassword = _userPassword.toPlainText()
#   userRole = _userRole.toPlainText()
#   userImage = _userImage.toPlainText()

#   query = 'INSERT INTO user(username,password,role,image) values(%s,%s,%s,%s)'
#   format = (userUserName, userPassword, userRole, userImage) 
#   execQuery(query,format=format,queryType="INSERT")
#   setupUserContent(_content_A_1)

def getJadwalOfMatkul(matkulId: str):
  global _jadwal_A_2
  semuaJadwal = []
  if(_jadwal_A_2 is None):
    _jadwal_A_2 = getJadwals()
  for jadwal in _jadwal_A_2:
    if(jadwal.kode_matkul == matkulId):
      semuaJadwal.append([jadwal.hari, jadwal.waktu_mulai, jadwal.waktu_selesai])
  return semuaJadwal


def getMatkuls():
  query = """SELECT * FROM mata_kuliah"""
  matkuls = execQuery(query)
  return matkuls

def getJadwals():
  query = """SELECT kode_matkul, waktu_mulai, waktu_selesai, hari FROM waktu NATURAL JOIN slot_waktu_jadwal NATURAL JOIN slot_waktu"""
  jadwals = execQuery(query)
  return jadwals
