from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from util.mysql_controller import execQuery


def setupDashboardContent(content, auth, profile, studyList):
    global _mainVLayout_M_3, _profileHLayout_M_3, _profilePicture_M_3, \
           _profileDetail_M_3, _profileDetailValue_M_3
    # Setup the query
    profile, studyList = setupQuery(auth, profile, studyList)

    # Assert that the query successful
    assert profile is not None
    assert studyList is not None

    # Get object from dashboard ui
    _scrollArea_M_3 = content.findChild(QScrollArea, "scrollArea_M_3")
    _mainVLayout_M_3 = content.findChild(QVBoxLayout, "mainVLayout_M_3")
    _profileHLayout_M_3 = content.findChild(QHBoxLayout, "profileHLayout_M_3")
    _profilePicture_M_3 = content.findChild(QLabel, "profilePicture_M_3")
    _profileDetail_M_3 = content.findChild(QLabel, "profileDetail_M_3")
    _profileDetailValue_M_3 = content.findChild(QLabel, "profileDetailValue_M_3")
    # Asserting object findChild successful
    assert _scrollArea_M_3 is not None
    assert _mainVLayout_M_3 is not None
    assert _profileHLayout_M_3 is not None
    assert _profilePicture_M_3 is not None
    assert _profileDetail_M_3 is not None
    assert _profileDetailValue_M_3 is not None
    # Set mainVLayout alignment
    _mainVLayout_M_3.setAlignment(Qt.AlignTop)
    mainScrollArea = QWidget()
    mainScrollArea.setLayout(_mainVLayout_M_3)
    mainScrollArea.setMaximumWidth(content.frameGeometry().width() - 300)
    _scrollArea_M_3.setAlignment(Qt.AlignHCenter)
    _scrollArea_M_3.setWidget(mainScrollArea)
    _scrollArea_M_3.setWidgetResizable(True)

    # Setup profile section
    setupProfileSection(content, profile)

    # Setup study section
    setupstudySection(content, studyList)

    # Return profile and study so it will be reusable
    return (profile, studyList)


def setupQuery(auth, profile, studyList):
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
    # If first time, get mahasiswa study list
    if studyList is None:
        try:
            query = """SELECT *
                       FROM (
                           mata_kuliah_diambil
                           NATURAL JOIN waktu
                           NATURAL JOIN mata_kuliah
                           NATURAL JOIN jadwal
                           NATURAL JOIN slot_waktu_jadwal
                           NATURAL JOIN slot_waktu
                       )
                       WHERE mata_kuliah_diambil.nim=%s"""
            format = (profile.nim,)
            studyList = execQuery(query, format)
        except Exception as e:
            print(e)
    return (profile, studyList)


def setupProfileSection(content, profile):
    global _profileHLayout_M_3, _profilePicture_M_3, \
           _profileDetail_M_3, _profileDetailValue_M_3
    # Set max profile height
    _profileHLayout_M_3.setAlignment(Qt.AlignTop)
    # Set profile picture
    _profilePicture_M_3.setPixmap(QPixmap(":img/img/profil_default.png"))
    _profilePicture_M_3.setFixedHeight(300)
    _profilePicture_M_3.setFixedWidth(300)
    # Set profile detail
    profileDetail = f"Nama\n" \
                    f"Angkatan\n" \
                    f"Tempat/Tanggal Lahir\n" \
                    f"IPK\n" \
                    f"NIM"
    _profileDetail_M_3.setText(profileDetail)
    _profileDetail_M_3.setFixedHeight(300)
    _profileDetail_M_3.setMinimumWidth(200)
    # Set profile detail value
    tempatTanggalLahir = profile.tempat_lahir + ", " + profile.tanggal_lahir.strftime("%m/%d/%Y");
    profileDetailValue = f": {profile.nama_mahasiswa}\n" \
                         f": {profile.angkatan}\n" \
                         f": {tempatTanggalLahir}\n" \
                         f": {4.00}\n" \
                         f": {profile.nim}"
    _profileDetailValue_M_3.setText(profileDetailValue)
    _profileDetailValue_M_3.setFixedHeight(300)
    _profileDetailValue_M_3.setMinimumWidth(content.frameGeometry().width() - 500)


def setupstudySection(content, studyList):
    global _mainVLayout_M_3
    # Add table header
    # Setup label
    header = QLabel()
    hBox = QHBoxLayout()
    header.setLayout(hBox)
    header.setFixedHeight(75)
    header.setStyleSheet("background-color: black")
    # Label style
    styleHeader = "font: 13pt Franklin Gothic Demi Cond; color: white"
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
    # Header Kehadiran Mata Kuliah
    hadirHeader = QLabel()
    hadirHeader.setText("Kehadiran")
    hadirHeader.setAlignment(Qt.AlignCenter)
    hadirHeader.setStyleSheet(styleHeader)
    # Header Nilai Mata Kuliah
    nilaiHeader = QLabel()
    nilaiHeader.setText("Nilai")
    nilaiHeader.setAlignment(Qt.AlignCenter)
    nilaiHeader.setStyleSheet(styleHeader)
    # Set in hBox
    hBox.addWidget(namaHeader)
    hBox.addWidget(matkulHeader)
    hBox.addWidget(hadirHeader)
    hBox.addWidget(nilaiHeader)
    # Set in mainVLayout
    _mainVLayout_M_3.addWidget(header)

    # Add table row
    # Label style
    styleRow = "font: 13pt Franklin Gothic Demi Cond; border: 1px solid blue"
    for study in studyList:
        # Setup label
        row = QLabel()
        hBox = QHBoxLayout()
        row.setLayout(hBox)
        row.setFixedHeight(75)
        row.setStyleSheet("border: 2px solid black")
        # Row Nama Mata Kuliah
        namaRow = QLabel()
        namaRow.setText(study.nama_matkul)
        namaRow.setAlignment(Qt.AlignCenter)
        namaRow.setStyleSheet(styleRow)
        # Row Jadwal Mata Kuliah
        matkulRow = QLabel()
        matkulRow.setText(study.hari + ", " + str(study.waktu_mulai) + " - " + str(study.waktu_selesai))
        matkulRow.setAlignment(Qt.AlignCenter)
        matkulRow.setStyleSheet(styleRow)
        # Row Kehadiran Mata Kuliah
        hadirRow = QLabel()
        hadirRow.setText(str(study.kehadiran) + "%")
        hadirRow.setAlignment(Qt.AlignCenter)
        hadirRow.setStyleSheet(styleRow)
        # Row Nilai Mata Kuliah
        nilaiRow = QLabel()
        nilaiRow.setText(study.indeks)
        nilaiRow.setAlignment(Qt.AlignCenter)
        nilaiRow.setStyleSheet(styleRow)
        # Set in hBox
        hBox.addWidget(namaRow)
        hBox.addWidget(matkulRow)
        hBox.addWidget(hadirRow)
        hBox.addWidget(nilaiRow)
        # Set in mainVLayout
        _mainVLayout_M_3.addWidget(row)
        
