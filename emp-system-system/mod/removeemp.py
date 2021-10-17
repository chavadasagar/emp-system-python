import mysql.connector
import mod.connection as con

obj = con.con

class remove_emp:
    def __init__(self,id):
        # data = (id)
        sql = f"delete from emp where id={id}"
        obj.cur.execute(sql)
        obj.mydb.commit()