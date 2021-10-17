import mysql.connector
import mod.connection as con

obj = con.con

class show_specific:
    data = []
    def __init__(self,idd):
        cur = obj.mydb.cursor()
        cur.execute(f"select * from emp where id={idd}")

        for rec in cur:
            dd = (rec[0],rec[1],rec[2],rec[3],rec[4])
            self.data.append(dd)

    def show(self):
        return self.data