from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from util.mysql_controller import execQuery

def setupUserContent(content, auth, profile, teachList):
    global _mainVLayout_D_3, _profileHLayout_D_3, _profilePicture_D_3, \
           _profileDetail_D_3, _profileDetailValue_D_3
#     # Assert that the query successful
#     assert profile is not None
#     assert teachList is not None

#     # Get object from dashboard ui
#     _scrollArea_D_3 = content.findChild(QScrollArea, "scrollArea_D_3")
#     _mainVLayout_D_3 = content.findChild(QVBoxLayout, "mainVLayout_D_3")
#     _profileHLayout_D_3 = content.findChild(QHBoxLayout, "profileHLayout_D_3")
#     _profilePicture_D_3 = content.findChild(QLabel, "profilePicture_D_3")
#     _profileDetail_D_3 = content.findChild(QLabel, "profileDetail_D_3")
#     _profileDetailValue_D_3 = content.findChild(QLabel, "profileDetailValue_D_3")
#     # Asserting object findChild successful
#     assert _scrollArea_D_3 is not None
#     assert _mainVLayout_D_3 is not None
#     assert _profileHLayout_D_3 is not None
#     assert _profilePicture_D_3 is not None
#     assert _profileDetail_D_3 is not None
#     assert _profileDetailValue_D_3 is not None
#     # Set mainVLayout alignment
#     _mainVLayout_D_3.setAlignment(Qt.AlignTop)
#     mainScrollArea = QWidget()
#     mainScrollArea.setLayout(_mainVLayout_D_3)
#     mainScrollArea.setMaximumWidth(content.frameGeometry().width() - 300)
#     _scrollArea_D_3.setAlignment(Qt.AlignHCenter)
#     _scrollArea_D_3.setWidget(mainScrollArea)
#     _scrollArea_D_3.setWidgetResizable(True)

#     # Setup profile section
#     setupProfileSection(content, profile)

#     # Setup teach section
#     setupTeachSection(content, teachList)

#     # Return profile and teach so it will be reusable
#     return (profile, teachList)
