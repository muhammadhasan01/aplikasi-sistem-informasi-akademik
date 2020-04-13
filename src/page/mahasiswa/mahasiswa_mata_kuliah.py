from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

from util.mysql_controller import execQuery


def setupMataKuliahContent(content, auth, profile, matkulList):
    global _mainVLayout_M_5
    # Setup the query
    profile, matkulList = setupQuery(auth, profile, matkulList)

    # Assert that the query successful
    assert profile is not None
    assert matkulList is not None

    # Get object from dashboard ui
    _scrollArea_M_5 = content.findChild(QScrollArea, "scrollArea_M_5")
    _mainVLayout_M_5 = content.findChild(QVBoxLayout, "mainVLayout_M_5")
    # Asserting object findChild successful
    assert _scrollArea_M_5 is not None
    assert _mainVLayout_M_5 is not None
    # Set mainVLayout alignment
    _mainVLayout_M_5.setAlignment(Qt.AlignTop)
    mainScrollArea = QWidget()
    mainScrollArea.setLayout(_mainVLayout_M_5)
    mainScrollArea.setMaximumWidth(content.frameGeometry().width() - 300)
    _scrollArea_M_5.setAlignment(Qt.AlignHCenter)
    _scrollArea_M_5.setWidget(mainScrollArea)
    _scrollArea_M_5.setWidgetResizable(True)

    # Setup matkul section
    setupMatkulSection(content, matkulList)

    # Return profile and matkul so it will be reusable
    return (profile, matkulList)


def setupQuery(auth, profile, matkulList):
    # If first time, get mahasiswa profile
    if profile is None:
        try:
            query = """SELECT *
                       FROM user JOIN profil_mahasiswa
                       ON user.id=profil_mahasiswa.user_id_mahasiswa
                       WHERE user.id=%s"""
            format = (auth.id,)
            profile = execQuery(query, format)[0]
        except Exception as e:
            print(e)
    # If first time, get mahasiswa matkul list
    if matkulList is None:
        try:
            query = """SELECT *
                       FROM (
                           mata_kuliah
                           NATURAL JOIN waktu
                           NATURAL JOIN jadwal
                           NATURAL JOIN slot_waktu_jadwal
                           NATURAL JOIN slot_waktu
                       )
                       WHERE mata_kuliah.kode_jurusan=%s"""
            format = (profile.kode_jurusan,)
            matkulList = execQuery(query, format)
        except Exception as e:
            print(e)
    return (profile, matkulList)


def setupMatkulSection(content, matkulList):
    global _mainVLayout_M_5
    print("Nah ini dia")
    print(matkulList)
    # Add table header
    # Setup label
    title = QLabel()
    header = QLabel()
    hBox = QHBoxLayout()
    header.setLayout(hBox)
    header.setFixedHeight(75)
    header.setStyleSheet("background-color: black")
    # Label style
    styleTitle = "font: 20pt Franklin Gothic Demi Cond"
    styleHeader = "font: 13pt Franklin Gothic Demi Cond; color: white"
    # Title Mata Kuliah yang dapat diambil
    title.setText("\nMata Kuliah yang Dapat Diambil")
    title.setAlignment(Qt.AlignLeft)
    title.setStyleSheet(styleTitle)
    # Header Nama Mata Kuliah
    namaHeader = QLabel()
    namaHeader.setText("Nama Mata Kuliah")
    namaHeader.setAlignment(Qt.AlignCenter)
    namaHeader.setStyleSheet(styleHeader)
    # Header Jadwal Mata Kuliah
    matkulHeader = QLabel()
    matkulHeader.setText("Jadwal")
    matkulHeader.setAlignment(Qt.AlignCenter)
    matkulHeader.setStyleSheet(styleHeader)
    # Header Daftar Mata Kuliah
    hadirHeader = QLabel()
    hadirHeader.setText("")
    hadirHeader.setAlignment(Qt.AlignCenter)
    hadirHeader.setStyleSheet(styleHeader)
    # Set in hBox
    hBox.addWidget(namaHeader)
    hBox.addWidget(matkulHeader)
    hBox.addWidget(hadirHeader)
    # Set in mainVLayout
    _mainVLayout_M_5.addWidget(title)
    _mainVLayout_M_5.addWidget(header)

    # Add table row
    # Label style
    styleRow = "font: 13pt Franklin Gothic Demi Cond; border: 1px solid blue"
    for matkul in matkulList:
        # Setup label
        row = QLabel()
        hBox = QHBoxLayout()
        row.setLayout(hBox)
        row.setFixedHeight(75)
        row.setStyleSheet("border: 2px solid black")
        # Row Nama Mata Kuliah
        namaRow = QLabel()
        namaRow.setText(matkul.nama_matkul)
        namaRow.setAlignment(Qt.AlignCenter)
        namaRow.setStyleSheet(styleRow)
        # Row Jadwal Mata Kuliah
        matkulRow = QLabel()
        matkulRow.setText(matkul.hari + ", " + str(matkul.waktu_mulai) + " - " + str(matkul.waktu_selesai))
        matkulRow.setAlignment(Qt.AlignCenter)
        matkulRow.setStyleSheet(styleRow)
        # Row Daftar Mata Kuliah
        daftarRow = QPushButton("Daftar")
        daftarRow.setCheckable(True)
        daftarRow.setStyleSheet(styleRow)
        # Set in hBox
        hBox.addWidget(namaRow)
        hBox.addWidget(matkulRow)
        hBox.addWidget(daftarRow)
        # Set in mainVLayout
        _mainVLayout_M_5.addWidget(row)
        
