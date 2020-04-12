# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_L_1(object):
    def setupUi(self, MainWindow_L_1):
        MainWindow_L_1.setObjectName("MainWindow_L_1")
        MainWindow_L_1.resize(1920, 1080)
        self.centralwidget_L_1 = QtWidgets.QWidget(MainWindow_L_1)
        self.centralwidget_L_1.setObjectName("centralwidget_L_1")
        self.loginButton_L_1 = QtWidgets.QPushButton(self.centralwidget_L_1)
        self.loginButton_L_1.setGeometry(QtCore.QRect(1250, 870, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(15)
        self.loginButton_L_1.setFont(font)
        self.loginButton_L_1.setStyleSheet("")
        self.loginButton_L_1.setObjectName("loginButton_L_1")
        self.usernameInput_L_1 = QtWidgets.QLineEdit(self.centralwidget_L_1)
        self.usernameInput_L_1.setGeometry(QtCore.QRect(1250, 660, 521, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.usernameInput_L_1.setFont(font)
        self.usernameInput_L_1.setObjectName("usernameInput_L_1")
        self.passwordInput_L_1 = QtWidgets.QLineEdit(self.centralwidget_L_1)
        self.passwordInput_L_1.setGeometry(QtCore.QRect(1250, 760, 521, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.passwordInput_L_1.setFont(font)
        self.passwordInput_L_1.setObjectName("passwordInput_L_1")
        self.loginBgLabel_L_1 = QtWidgets.QLabel(self.centralwidget_L_1)
        self.loginBgLabel_L_1.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.loginBgLabel_L_1.setText("")
        self.loginBgLabel_L_1.setScaledContents(True)
        self.loginBgLabel_L_1.setObjectName("loginBgLabel_L_1")
        self.forgotPasswordButton_L_1 = QtWidgets.QPushButton(self.centralwidget_L_1)
        self.forgotPasswordButton_L_1.setGeometry(QtCore.QRect(1520, 870, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(15)
        self.forgotPasswordButton_L_1.setFont(font)
        self.forgotPasswordButton_L_1.setObjectName("forgotPasswordButton_L_1")
        self.signInLabel_L_1 = QtWidgets.QLabel(self.centralwidget_L_1)
        self.signInLabel_L_1.setGeometry(QtCore.QRect(1250, 570, 521, 71))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(25)
        self.signInLabel_L_1.setFont(font)
        self.signInLabel_L_1.setAlignment(QtCore.Qt.AlignCenter)
        self.signInLabel_L_1.setObjectName("signInLabel_L_1")
        self.loginBgLabel_L_1.raise_()
        self.loginButton_L_1.raise_()
        self.usernameInput_L_1.raise_()
        self.passwordInput_L_1.raise_()
        self.forgotPasswordButton_L_1.raise_()
        self.signInLabel_L_1.raise_()
        MainWindow_L_1.setCentralWidget(self.centralwidget_L_1)
        self.menubar_L_1 = QtWidgets.QMenuBar(MainWindow_L_1)
        self.menubar_L_1.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar_L_1.setObjectName("menubar_L_1")
        MainWindow_L_1.setMenuBar(self.menubar_L_1)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_L_1)
        self.statusbar.setObjectName("statusbar")
        MainWindow_L_1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_L_1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_L_1)

    def retranslateUi(self, MainWindow_L_1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_L_1.setWindowTitle(_translate("MainWindow_L_1", "MainWindow"))
        self.loginButton_L_1.setText(_translate("MainWindow_L_1", "Login"))
        self.usernameInput_L_1.setPlaceholderText(_translate("MainWindow_L_1", "Username"))
        self.passwordInput_L_1.setPlaceholderText(_translate("MainWindow_L_1", "Password"))
        self.forgotPasswordButton_L_1.setText(_translate("MainWindow_L_1", "Forgot Password"))
        self.signInLabel_L_1.setText(_translate("MainWindow_L_1", "Sign In"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_L_1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_L_1()
    ui.setupUi(MainWindow_L_1)
    MainWindow_L_1.show()
    sys.exit(app.exec_())
