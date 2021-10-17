import mysql.connector


class con:
    mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "",
    database = "info"
    )

    cur = mydb.cursor()