from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from util.mysql_controller import execQuery


def setupDashboardContent(content, auth, profile, teach):
    profile, teach = setupQuery(auth, profile, teach)
    # Get object from dashboard ui
    _mainVLayout_D_3 = content.findChild(QVBoxLayout, "mainVLayout_D_3")
    _profileHLayout_D_3 = content.findChild(QHBoxLayout, "profileHLayout_D_3")
    _profilePicture_D_3 = content.findChild(QLabel, "profilePicture_D_3")
    _profileDetail_D_3 = content.findChild(QLabel, "profileDetail_D_3")
    _profileDetailValue_D_3 = content.findChild(QLabel, "profileDetailValue_D_3")
    # Asserting object findChild successful
    assert _mainVLayout_D_3 is not None
    assert _profileHLayout_D_3 is not None
    assert _profilePicture_D_3 is not None
    assert _profileDetail_D_3 is not None
    assert _profileDetailValue_D_3 is not None

    # Set max profile height
    _profileHLayout_D_3.setAlignment(Qt.AlignTop)
    # Set profile picture
    _profilePicture_D_3.setPixmap(QPixmap(":img/img/profil_default.png"))
    _profilePicture_D_3.setFixedHeight(300)
    _profilePicture_D_3.setFixedWidth(300)
    # Set profile detail
    profileDetail = f"""\
Nama
NIP
No HP
Email"""
    _profileDetail_D_3.setText(profileDetail)
    _profileDetail_D_3.setFixedHeight(300)
    _profileDetail_D_3.setMinimumWidth(200)
    # Set profile detail value
    profileDetailValue = f"""\
: {profile.nama_dosen}
: {profile.NIP}
: {profile.no_hp}
: {profile.email}"""
    _profileDetailValue_D_3.setText(profileDetailValue)
    _profileDetailValue_D_3.setFixedHeight(300)
    _profileDetailValue_D_3.setMinimumWidth(content.frameGeometry().width() - 500)

    # Return profile and teach so it will be reusable
    return (profile, teach)


def setupQuery(auth, profile, teach):
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
    # If first time, get dosen profile
    if teach is None:
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
            teach = execQuery(query, format)[0]
        except Exception as e:
            print(e)
    return (profile, teach)
