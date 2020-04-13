from PyQt5.QtWidgets import QPushButton, QLineEdit

from util.mysql_controller import execQuery, getDatabase


def setupCreateStdAccountContent(content, auth, profile):
    global _nimInput_D_5, _angkatanInput_D_5, _namaInput_D_5, \
           _tempatLahirInput_D_5, _tanggalLahirInput_D_5, _alamatRumahInput_D_5, \
           _alamatTinggalInput_D_5, _emailInput_D_5, _kodeJurusanInput_D_5, \
           _userDefaultInput_D_5, _passDefaultInput_D_5
    # Setup the query
    profile = setupQuery(auth, profile)
    # Assert that the query successful
    assert profile is not None

    # Get object from dashboard ui
    _nimInput_D_5 = content.findChild(QLineEdit, "nimInput_D_5")
    _angkatanInput_D_5 = content.findChild(QLineEdit, "angkatanInput_D_5")
    _namaInput_D_5 = content.findChild(QLineEdit, "namaInput_D_5")
    _tempatLahirInput_D_5 = content.findChild(QLineEdit, "tempatLahirInput_D_5")
    _tanggalLahirInput_D_5 = content.findChild(QLineEdit, "tanggalLahirInput_D_5")
    _alamatRumahInput_D_5 = content.findChild(QLineEdit, "alamatRumahInput_D_5")
    _alamatTinggalInput_D_5 = content.findChild(QLineEdit, "alamatTinggalInput_D_5")
    _emailInput_D_5 = content.findChild(QLineEdit, "emailInput_D_5")
    _kodeJurusanInput_D_5 = content.findChild(QLineEdit, "kodeJurusanInput_D_5")
    _userDefaultInput_D_5 = content.findChild(QLineEdit, "userDefaultInput_D_5")
    _passDefaultInput_D_5 = content.findChild(QLineEdit, "passDefaultInput_D_5")
    _resetButton_D_5 = content.findChild(QPushButton, "resetButton_D_5")
    _submitButton_D_5 = content.findChild(QPushButton, "submitButton_D_5")
    # Asserting object findChild successful
    assert _nimInput_D_5 is not None
    assert _angkatanInput_D_5 is not None
    assert _namaInput_D_5 is not None
    assert _tempatLahirInput_D_5 is not None
    assert _tanggalLahirInput_D_5 is not None
    assert _alamatRumahInput_D_5 is not None
    assert _alamatTinggalInput_D_5 is not None
    assert _emailInput_D_5 is not None
    assert _kodeJurusanInput_D_5 is not None
    assert _userDefaultInput_D_5 is not None
    assert _passDefaultInput_D_5 is not None
    assert _resetButton_D_5 is not None
    assert _submitButton_D_5 is not None

    # Set connection
    _resetButton_D_5.clicked.connect(lambda: resetButtonClicked())
    _submitButton_D_5.clicked.connect(lambda: submitButtonClicked(profile))


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
    global _nimInput_D_5, _angkatanInput_D_5, _namaInput_D_5, \
           _tempatLahirInput_D_5, _tanggalLahirInput_D_5, _alamatRumahInput_D_5, \
           _alamatTinggalInput_D_5, _emailInput_D_5, _kodeJurusanInput_D_5, \
           _userDefaultInput_D_5, _passDefaultInput_D_5
    _nimInput_D_5.clear()
    _angkatanInput_D_5.clear()
    _namaInput_D_5.clear()
    _tempatLahirInput_D_5.clear()
    _tanggalLahirInput_D_5.clear()
    _alamatRumahInput_D_5.clear()
    _alamatTinggalInput_D_5.clear()
    _emailInput_D_5.clear()
    _kodeJurusanInput_D_5.clear()
    _userDefaultInput_D_5.clear()
    _passDefaultInput_D_5.clear()


def submitButtonClicked(profile):
    global _nimInput_D_5, _angkatanInput_D_5, _namaInput_D_5, \
           _tempatLahirInput_D_5, _tanggalLahirInput_D_5, _alamatRumahInput_D_5, \
           _alamatTinggalInput_D_5, _emailInput_D_5, _kodeJurusanInput_D_5, \
           _userDefaultInput_D_5, _passDefaultInput_D_5
    # Get value
    nim = _nimInput_D_5.displayText()
    angkatan = _angkatanInput_D_5.displayText()
    nama = _namaInput_D_5.displayText()
    tempatLahir = _tempatLahirInput_D_5.displayText()
    tanggalLahir = _tanggalLahirInput_D_5.displayText()
    alamatRumah = _alamatRumahInput_D_5.displayText()
    alamatTinggal = _alamatTinggalInput_D_5.displayText()
    email = _emailInput_D_5.displayText()
    kodeJurusan = _kodeJurusanInput_D_5.displayText()
    userDefault = _userDefaultInput_D_5.displayText()
    passDefault = _passDefaultInput_D_5.displayText()
    # Check if username or nim duplicate
    try:
        userList = execQuery("""SELECT username
                                FROM user
                                WHERE username=%s""",
                             (userDefault,))
        if userList:
            _nimInput_D_5.setText("Username sudah ada")
            print("Username sudah ada")
            return
        mhsList = execQuery("""SELECT nim
                               FROM profil_mahasiswa
                               WHERE nim=%s""",
                            (nim,))
        if mhsList:
            _nimInput_D_5.setText("NIM sudah ada")
            print("NIM sudah ada")
            return
    except Exception as e:
        print(e)
        return
    # Insert query to user table
    try:
        query = """INSERT INTO user (username, password, role, image)
                   VALUES (%s, %s, %s, %s)"""
        format = (userDefault, passDefault, "mahasiswa", "-",)
        db = getDatabase()
        cursor = db.cursor()
        cursor.execute(query, format)
        db.commit()
        # Get user id
        query = """SELECT id FROM user WHERE username=%s"""
        format = (userDefault,)
        id = execQuery(query, format)[0].id
    except Exception as e:
        print(e)
        return
    # Insert query to profil_mahasiswa table
    try:
        # (nim, angkatan, nama_mahasiswa, tempat_lahir, tanggal_lahir,
        # alamat_rumah, alamat_tinggal, email, user_id_mahasiswa, kode_jurusan,
        # nip_dosen_wali)
        query = """INSERT INTO profil_mahasiswa
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        format = (nim, angkatan, nama, tempatLahir, tanggalLahir, alamatRumah,
                  alamatTinggal, email, id, kodeJurusan, profile.NIP)
        print(format)
        db = getDatabase()
        cursor = db.cursor()
        cursor.execute(query, format)
        db.commit()
    except Exception as e:
        # Rollback user table
        query = """DELETE FROM user WHERE username=%s"""
        format = (userDefault,)
        db = getDatabase()
        cursor = db.cursor()
        cursor.execute(query, format)
        db.commit()
        print(e)
