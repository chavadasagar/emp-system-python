import mod.connection as con
import mysql.connector


# login class is used to check user is valid or not using isvalid method
# is valid method return true if user is valid anotherwise return false


con = con.con

class login:
    def isvalid(self,username,password):
        cur = con.mydb.cursor()
        data = (username,password)
        cur.execute("select username,password from user where username=%s and password=%s",data)
        s = cur.fetchall()

        if(data in s):
            return True
        else:
            return False



