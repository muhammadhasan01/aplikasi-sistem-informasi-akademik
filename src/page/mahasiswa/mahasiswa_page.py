from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5 import uic

import resource
from page.mahasiswa.mahasiswa_dashboard import setupDashboardContent
from page.mahasiswa.mahasiswa_mata_kuliah import setupMataKuliahContent


_auth = None
_mahasiswaProfile = None
_mahasiswaStudyList = None
_mahasiswaMataKuliah = None


def initMahasiswaPage(window, auth):
    global _navbar_M_1, _content_M_1, _mainVLayout_M_1, _auth
    # Save authentication profile
    _auth = auth
    # Load layout ui
    uifile = QFile(":ui/ui/mahasiswa_layout.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, window)
    uifile.close()
    # Get object from layout ui
    _mainVLayout_M_1 = window.findChild(QVBoxLayout, "mainVLayout_M_1")

    # Create and load navbar widget
    _navbar_M_1 = QWidget()
    uifile = QFile(":ui/ui/mahasiswa_navbar.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, _navbar_M_1)
    uifile.close()
    # Get object from navbar ui
    _logoSiak_M_2 = _navbar_M_1.findChild(QLabel, "logoSiak_M_2")
    _berandaButton_M_2 = _navbar_M_1.findChild(QPushButton, "berandaButton_M_2")
    _pengaturanButton_M_2 = _navbar_M_1.findChild(QPushButton, "pengaturanButton_M_2")
    _mataKuliahButton_M_2 = _navbar_M_1.findChild(QPushButton, "mataKuliahButton_M_2")
    # Asserting object findChild successful
    assert _berandaButton_M_2 is not None
    assert _pengaturanButton_M_2 is not None
    assert _mataKuliahButton_M_2 is not None
    # Set logo
    _logoSiak_M_2.setPixmap(QPixmap(":img/img/logo_siak_full.png"))
    # Create and load content dashboard widget
    _content_M_1 = QWidget()
    uifile = QFile(":ui/ui/mahasiswa_content_dashboard.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, _content_M_1)
    uifile.close()
    # Simulate berandaButtonClicked
    berandaButtonClicked()

    # Set widgets to layout
    _mainVLayout_M_1.addWidget(_navbar_M_1)
    _mainVLayout_M_1.addWidget(_content_M_1)
    _navbar_M_1.setFixedHeight(200)
    _content_M_1.setMinimumHeight(window.frameGeometry().height() - 200)

    # Set connection
    _berandaButton_M_2.clicked.connect(lambda: berandaButtonClicked())
    _pengaturanButton_M_2.clicked.connect(lambda: pengaturanButtonClicked())
    _mataKuliahButton_M_2.clicked.connect(lambda: mataKuliahButtonClicked())


def berandaButtonClicked():
    global _content_M_1, _mainVLayout_M_1, _auth, _mahasiswaProfile, _mahasiswaStudyList
    # Create new widget
    newWidget = QWidget()
    uifile = QFile(":ui/ui/mahasiswa_content_dashboard.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, newWidget)
    uifile.close()
    _mahasiswaProfile, _mahasiswaStudyList = \
        setupDashboardContent(newWidget, _auth, _mahasiswaProfile, _mahasiswaStudyList)
    # Set up the new widget
    _mainVLayout_M_1.removeWidget(_content_M_1)
    _content_M_1 = newWidget
    _mainVLayout_M_1.addWidget(_content_M_1)


def pengaturanButtonClicked():
    global _content_M_1, _mainVLayout_M_1
    # Create new widget
    newWidget = QWidget()
    uifile = QFile(":ui/ui/mahasiswa_content_settings.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, newWidget)
    uifile.close()
    # Set up the new widget
    _mainVLayout_M_1.removeWidget(_content_M_1)
    _content_M_1 = newWidget
    _mainVLayout_M_1.addWidget(_content_M_1)


def mataKuliahButtonClicked():
    global _content_M_1, _mainVLayout_M_1, _auth, _mahasiswaProfile, _mahasiswaMataKuliah
    # Create new widget
    newWidget = QWidget()
    uifile = QFile(":ui/ui/mahasiswa_content_matkul.ui")
    uifile.open(QFile.ReadOnly)
    uic.loadUi(uifile, newWidget)
    uifile.close()
    _mahasiswaProfile, _mahasiswaMataKuliah = \
        setupMataKuliahContent(newWidget, _auth, _mahasiswaProfile, _mahasiswaMataKuliah)
    # Set up the new widget
    _mainVLayout_M_1.removeWidget(_content_M_1)
    _content_M_1 = newWidget
    _mainVLayout_M_1.addWidget(_content_M_1)
