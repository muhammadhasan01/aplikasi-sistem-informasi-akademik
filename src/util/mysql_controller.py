import mysql.connector


_mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="xFverzMDrj",
  passwd="9LyFkYxdKw",
  database="xFverzMDrj"
)


def execQuery(query):
    mycursor = _mydb.cursor(named_tuple=True)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult


def getDatabase():
    return _mydb
