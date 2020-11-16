import mysql.connector


_mydb = mysql.connector.connect(
    host="remotemysql.com",
    user="xFverzMDrj",
    passwd="9LyFkYxdKw",
    database="xFverzMDrj"
)

def execQuery(query, format=None, queryType="SELECT"):
  if not(_mydb.is_connected()):
        restartConnection()
  if(queryType == "SELECT"):
    mycursor = _mydb.cursor(named_tuple=True)
    mycursor.execute(query, format)
    myresult = mycursor.fetchall()
    return myresult
  elif(queryType == "INSERT" or queryType == "DELETE"):
    mycursor = _mydb.cursor(named_tuple=True)
    mycursor.execute(query, format)
    _mydb.commit()

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
