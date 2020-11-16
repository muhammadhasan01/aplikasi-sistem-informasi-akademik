from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from util.mysql_controller import execQuery


def setupDashboardContent(content, auth, profile, teachList):
    global _mainVLayout_D_3, _profileHLayout_D_3, _profilePicture_D_3, \
           _profileDetail_D_3, _profileDetailValue_D_3
    # Setup the query
    profile, teachList = setupQuery(auth, profile, teachList)
    # Assert that the query successful
    assert profile is not None
    assert teachList is not None

    # Get object from dashboard ui
    _scrollArea_D_3 = content.findChild(QScrollArea, "scrollArea_D_3")
    _mainVLayout_D_3 = content.findChild(QVBoxLayout, "mainVLayout_D_3")
    _profileHLayout_D_3 = content.findChild(QHBoxLayout, "profileHLayout_D_3")
    _profilePicture_D_3 = content.findChild(QLabel, "profilePicture_D_3")
    _profileDetail_D_3 = content.findChild(QLabel, "profileDetail_D_3")
    _profileDetailValue_D_3 = content.findChild(QLabel, "profileDetailValue_D_3")
    # Asserting object findChild successful
    assert _scrollArea_D_3 is not None
    assert _mainVLayout_D_3 is not None
    assert _profileHLayout_D_3 is not None
    assert _profilePicture_D_3 is not None
    assert _profileDetail_D_3 is not None
    assert _profileDetailValue_D_3 is not None
    # Set mainVLayout alignment
    _mainVLayout_D_3.setAlignment(Qt.AlignTop)
    mainScrollArea = QWidget()
    mainScrollArea.setLayout(_mainVLayout_D_3)
    mainScrollArea.setMaximumWidth(content.frameGeometry().width() - 300)
    _scrollArea_D_3.setAlignment(Qt.AlignHCenter)
    _scrollArea_D_3.setWidget(mainScrollArea)
    _scrollArea_D_3.setWidgetResizable(True)

    # Setup profile section
    setupProfileSection(content, profile)

    # Setup teach section
    setupTeachSection(content, teachList)

    # Return profile and teach so it will be reusable
    return (profile, teachList)


def setupQuery(auth, profile, teachList):
    # If first time, get dosen profile
    if profile is None:
        try:
            query = """SELECT *
                       FROM user JOIN profil_dosen
                       ON user.id=profil_dosen.user_id_dosen
                       WHERE user.id=%s"""
            format = (auth.id,)
            profile = execQuery(query, format)[0]
        except Exception as e:
            print(e)
    # If first time, get dosen teach list
    if teachList is None:
        try:
            query = """SELECT *
                       FROM (
                           mata_kuliah_diampu
                           NATURAL JOIN waktu
                           NATURAL JOIN mata_kuliah
                           NATURAL JOIN jadwal
                           NATURAL JOIN slot_waktu_jadwal
                           NATURAL JOIN slot_waktu
                       )
                       WHERE mata_kuliah_diampu.nip=%s"""
            format = (profile.NIP,)
            teachList = execQuery(query, format)
        except Exception as e:
            print(e)
    return (profile, teachList)


def setupProfileSection(content, profile):
    global _profileHLayout_D_3, _profilePicture_D_3, \
           _profileDetail_D_3, _profileDetailValue_D_3
    # Set max profile height
    _profileHLayout_D_3.setAlignment(Qt.AlignTop)
    # Set profile picture
    _profilePicture_D_3.setPixmap(QPixmap(":img/img/profil_default.png"))
    _profilePicture_D_3.setFixedHeight(300)
    _profilePicture_D_3.setFixedWidth(300)
    # Set profile detail
    profileDetail = f"Nama\n" \
                    f"NIP\n" \
                    f"No HP\n" \
                    f"Email"
    _profileDetail_D_3.setText(profileDetail)
    _profileDetail_D_3.setFixedHeight(300)
    _profileDetail_D_3.setMinimumWidth(200)
    # Set profile detail value
    profileDetailValue = f": {profile.nama_dosen}\n" \
                         f": {profile.NIP}\n" \
                         f": {profile.no_hp}\n" \
                         f": {profile.email}"
    _profileDetailValue_D_3.setText(profileDetailValue)
    _profileDetailValue_D_3.setFixedHeight(300)
    _profileDetailValue_D_3.setMinimumWidth(content.frameGeometry().width() - 500)


def setupTeachSection(content, teachList):
    global _mainVLayout_D_3
    # Add table header
    # Setup label
    header = QLabel()
    hBox = QHBoxLayout()
    header.setLayout(hBox)
    header.setFixedHeight(75)
    header.setStyleSheet("background-color: black")
    # Label style
    styleHeader = "font: 13pt Franklin Gothic Demi Cond; color: white"
    # Left
    lHeader = QLabel()
    lHeader.setText("Nama Mata Kuliah")
    lHeader.setAlignment(Qt.AlignCenter)
    lHeader.setStyleSheet(styleHeader)
    # Right
    rHeader = QLabel()
    rHeader.setText("Jadwal")
    rHeader.setAlignment(Qt.AlignCenter)
    rHeader.setStyleSheet(styleHeader)
    # Set in hBox
    hBox.addWidget(lHeader)
    hBox.addWidget(rHeader)
    # Set in mainVLayout
    _mainVLayout_D_3.addWidget(header)

    # Add table row
    # Label style
    styleRow = "font: 13pt Franklin Gothic Demi Cond; border: 1px solid blue"
    for teach in teachList:
        # Setup label
        row = QLabel()
        hBox = QHBoxLayout()
        row.setLayout(hBox)
        row.setFixedHeight(75)
        row.setStyleSheet("border: 2px solid black")
        # Left
        lRow = QLabel()
        lRow.setText(teach.nama_matkul)
        lRow.setAlignment(Qt.AlignCenter)
        lRow.setStyleSheet(styleRow)
        # Right
        rRow = QLabel()
        rRow.setText(str(teach.waktu_mulai) + " - " + str(teach.waktu_selesai))
        rRow.setAlignment(Qt.AlignCenter)
        rRow.setStyleSheet(styleRow)
        # Set in hBox
        hBox.addWidget(lRow)
        hBox.addWidget(rRow)
        # Set in mainVLayout
        _mainVLayout_D_3.addWidget(row)
