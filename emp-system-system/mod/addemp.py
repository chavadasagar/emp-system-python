import mysql.connector
import mod.connection as con

# create objetct con class
obj = con.con
# this class is use to add employee using constructor
class addemp:
    def __init__(self,emp_name, age, phno, gender):
        data = (emp_name,age,phno,gender)
        sql = "INSERT INTO emp(emp_name,age,phno,gender) VALUES (%s,%s,%s,%s)"
        obj.cur.execute(sql,data)
        obj.mydb.commit()   