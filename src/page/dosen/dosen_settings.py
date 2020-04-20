from PyQt5.QtWidgets import QPushButton, QLineEdit, QMessageBox

from util.mysql_controller import execQuery, getDatabase


def setupSettingsContent(content, auth, profile):
    global _userLamaInput_D_4, _passLamaInput_D_4, _userBaruInput_D_4, \
           _passBaruInput_D_4, _resetButton_D_4, _submitButton_D_4
    # Setup the query
    profile = setupQuery(auth, profile)
    # Assert that the query successful
    assert profile is not None

    # Get object from dashboard ui
    _userLamaInput_D_4 = content.findChild(QLineEdit, "userLamaInput_D_4")
    _passLamaInput_D_4 = content.findChild(QLineEdit, "passLamaInput_D_4")
    _userBaruInput_D_4 = content.findChild(QLineEdit, "userBaruInput_D_4")
    _passBaruInput_D_4 = content.findChild(QLineEdit, "passBaruInput_D_4")
    _resetButton_D_4 = content.findChild(QPushButton, "resetButton_D_4")

    # Asserting object findChild successful
    assert _userLamaInput_D_4 is not None
    assert _passLamaInput_D_4 is not None
    assert _userBaruInput_D_4 is not None
    assert _passBaruInput_D_4 is not None
    assert _resetButton_D_4 is not None

    # Masking password
    _passLamaInput_D_4.setEchoMode(QLineEdit.Password)
    _passBaruInput_D_4.setEchoMode(QLineEdit.Password)

    # Set connection
    _resetButton_D_4.clicked.connect(lambda: resetButtonClicked())

    # Return profile so it will be reusable
    return profile


def setupQuery(auth, profile):
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
    return profile


def resetButtonClicked():
    global _userLamaInput_D_4, _passLamaInput_D_4, _userBaruInput_D_4, \
           _passBaruInput_D_4
    _userLamaInput_D_4.clear()
    _passLamaInput_D_4.clear()
    _userBaruInput_D_4.clear()
    _passBaruInput_D_4.clear()


def submitButtonClicked(profile):
    global _userLamaInput_D_4, _passLamaInput_D_4, _userBaruInput_D_4, \
           _passBaruInput_D_4
    oldUser = _userLamaInput_D_4.displayText()
    oldPass = _passLamaInput_D_4.displayText()
    newUser = _userBaruInput_D_4.displayText()
    newPass = _passBaruInput_D_4.displayText()
    message = QMessageBox()
    message.setIcon(QMessageBox.Information)
    # Check old user and old pass input
    if oldUser != profile.username or oldPass != profile.password:
        message.setWindowTitle("Invalid input")
        message.setText("Old username or password is invalid")
        message.exec_()
        return profile
    # Old data valid
    try:
        query = """UPDATE user
                   SET username=%s, password=%s
                   WHERE id=%s"""
        format = (newUser, newPass, profile.id,)
        # Update database
        db = getDatabase()
        cursor = db.cursor()
        cursor.execute(query, format)
        db.commit()
        # Update profile
        profile = profile._replace(username=newUser, password=newPass)
    except Exception as e:
        print(e)
        message.setWindowTitle("Invalid input")
        message.setText("New username or password is invalid")
        message.exec_()
    # Print message
    message.setWindowTitle("Process successful")
    message.setText("User successfully updated")
    message.exec_()
    # Return profile so it can be reused
    return profile
