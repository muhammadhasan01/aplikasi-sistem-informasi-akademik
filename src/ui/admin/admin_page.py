# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpageadmin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_A_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 880)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 110, 341, 231))
        font = QtGui.QFont()
        font.setPointSize(52)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.nama_admin = QtWidgets.QLabel(self.centralwidget)
        self.nama_admin.setGeometry(QtCore.QRect(800, 110, 341, 231))
        font = QtGui.QFont()
        font.setPointSize(52)
        self.nama_admin.setFont(font)
        self.nama_admin.setObjectName("nama_admin")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Nama : "))
        self.nama_admin.setText(_translate("MainWindow", "ADMIN"))
import mainpage_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
