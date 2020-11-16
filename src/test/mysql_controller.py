import mysql.connector


_mydb = mysql.connector.connect(
    host="remotemysql.com",
    user="xFverzMDrj",
    passwd="9LyFkYxdKw",
    database="xFverzMDrj"
)


def execQuery(query, format=None):
    if not(_mydb.is_connected()):
        restartConnection()
    mycursor = _mydb.cursor(named_tuple=True)
    mycursor.execute(query, format)
    myresult = mycursor.fetchall()
    return myresult


def getDatabase():
    if not(_mydb.is_connected()):
        restartConnection()
    return _mydb


def restartConnection():
    global _mydb
    _mydb = mysql.connector.connect(
        host="remotemysql.com",
        user="xFverzMDrj",
        passwd="9LyFkYxdKw",
        database="xFverzMDrj"
    )
