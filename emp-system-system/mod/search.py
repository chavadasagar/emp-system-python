import mysql.connector
import mod.connection as con 


# this class is used to pass the name in constructor aygument
# and data method is return all info abount search list format

obj = con.con

class search:
    
    #store all search data in this list
    def data(self,name):
        search = []
        data = (name)
        cur = obj.mydb.cursor()
        cur.execute(f"select * from emp where emp_name like '%{name}%'")

        for rec in cur:
            data = (rec[0],rec[1],rec[2],rec[3],rec[4])
            search.append(data)
            obj.mydb.commit()

        return search