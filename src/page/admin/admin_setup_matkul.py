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
    _addMatkul_A_2.clicked.connect(lambda: showAddMatkulPopup())

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

  removeButton.clicked.connect(lambda : removeMatkulAndRender(matkul.kode_matkul))
  # updateButton.clicked.connect(lambda : showUpdatePopup())


def showAddMatkulPopup():
  global _addMatkulPopup_A_2
  _addMatkulPopup_A_2 = QWidget()
  uifile = QFile(":ui/ui/admin/admin_content_add_matkul.ui")
  uifile.open(QFile.ReadOnly)
  uic.loadUi(uifile, _addMatkulPopup_A_2)
  uifile.close()

  _addMatkulPopup_A_2.setFixedHeight(645)
  _addMatkulPopup_A_2.setFixedWidth(1000)

  _submit_form_A_2 = _addMatkulPopup_A_2.findChild(QPushButton, "submitButton")
  _submit_form_A_2.clicked.connect(lambda:insertMatkulToDatabaseAndRenderPage())
  _addMatkulPopup_A_2.show()

def removeMatkulAndRender(matkulId):
  global _content_A_2
  query = "DELETE FROM mata_kuliah WHERE kode_matkul = %s"
  format = (matkulId,)
  execQuery(query,format=format,queryType="DELETE")
  setupMatkulContent(_content_A_2)


def insertMatkulToDatabaseAndRenderPage():
  global _addMatkulPopup_A_2, _content_A_2
  _matkulCode = _addMatkulPopup_A_2.findChild(QTextEdit, "matkulCode")
  _matkulName = _addMatkulPopup_A_2.findChild(QTextEdit, "matkulName")
  _matkulDescription = _addMatkulPopup_A_2.findChild(QTextEdit, "matkulDescription")
  _jurusanCode = _addMatkulPopup_A_2.findChild(QTextEdit, "jurusanCode")

  matkulCode = _matkulCode.toPlainText()
  matkulName = _matkulName.toPlainText()
  matkulDescription = _matkulDescription.toPlainText()
  jurusanCode = _jurusanCode.toPlainText()

  query = 'INSERT INTO mata_kuliah(kode_matkul,nama_matkul,deskripsi_matkul,kode_jurusan) values(%s,%s,%s,%s)'
  format = (matkulCode, matkulName, matkulDescription, jurusanCode) 
  execQuery(query,format=format,queryType="INSERT")
  setupMatkulContent(_content_A_2)

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
