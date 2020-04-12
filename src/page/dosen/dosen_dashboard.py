from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QLabel


def setupDashboardContent(content, auth):
    # Get object from dashboard ui
    _mainVLayout_D_3 = content.findChild(QVBoxLayout, "mainVLayout_D_3")
    _profilePicture_D_3 = content.findChild(QLabel, "profilePicture_D_3")
    _profileDetail_D_3 = content.findChild(QLabel, "profileDetail_D_3")
    # Asserting object findChild successful
    assert _mainVLayout_D_3 is not None
    assert _profilePicture_D_3 is not None
    assert _profileDetail_D_3 is not None

    # Set profile picture
    _profilePicture_D_3.setPixmap(QPixmap(":img/img/profil_default.png"))
    _profilePicture_D_3.setFixedHeight(300)
    _profilePicture_D_3.setFixedWidth(300)
    # Set profile detail
    profileText = f"""\
Nama    : {auth.username}
NIP     : {auth.role}\
"""
    _profileDetail_D_3.setText(profileText)
    _profileDetail_D_3.setFixedHeight(300)
    _profileDetail_D_3.setFixedHeight(300)
    _profileDetail_D_3.setMinimumWidth(content.frameGeometry().width() - 300)
