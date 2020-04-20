import mysql.connector


_mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="xFverzMDrj",
  passwd="9LyFkYxdKw",
  database="xFverzMDrj"
)


def execQuery(query, format=None, queryType="SELECT"):
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
    return _mydb