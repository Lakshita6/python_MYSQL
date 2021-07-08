import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root',
        password='lakshitasql123456',database='pyhontest')

        query='create table if not exists user(userId int primary key,username varchar(200),phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Table created")

#Insert
    def insert_user(self, userid, username, phone):
        query = "insert into user(userId,userName,phone) values({},'{}','{}')".format(
            userid, username, phone)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    #fetch
    def fetch_all(self):
        query = "select * from user" 
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id :", row[0])
            print("User Name :", row[1])
            print("User Phone :", row[2])
            print()
            print()


        
        
#maincode
helper= DBHelper()
#helper.insert_user(8746,'Lakshita',"456736")
#helper.insert_user(9364,'priya',"947820")
#helper.insert_user(9386,'ankit',"349098")
#helper.insert_user(8564,'riya',"465372")
#helper.insert_user(4352,'akshit',"78463")

helper.fetch_all()

