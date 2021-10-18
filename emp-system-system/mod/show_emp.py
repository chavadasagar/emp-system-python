import mysql.connector
import mod.connection as con

obj = con.con


class show_emp:
    data = []
    def __init__(self):
        cur = obj.mydb.cursor()

        q = cur.execute("select * from emp")

        for rec in cur:
            r = (rec[0],rec[1],rec[2],rec[3],rec[4])
            self.data.append(r)
        
    def alldata(self):
        return self.data
    def clear(self):
        self.data.clear()

        