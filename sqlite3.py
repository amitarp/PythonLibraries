import mysql.connector as connector


class DBhelper:
    def __init__(self) -> None:
        self.con=connector.connect(host='localhost',port='3306',user='root',password='prats17',database='python')
        query='create table if not exists user(userId int primary key,userName varchar(200),phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print("created")

    #inserting method
    def insert_user(self,userid,username,phone):
        query="insert into user(userId,userName,phone) values({},'{}','{}')".format(userid,username,phone)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user save to db")

    #fetch all
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)

    #Deleting rows
    def delete_row(self,userid):
        query="delete from user where userId={}".format(userid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")

    #for updating
    def update_row(self,userid, newName,newPhone):
        query="update user set userName='{}',phone='{}' where userId={}".format(newName,newPhone,userid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")

#manin coding

helper=DBhelper()
helper.update_row(3, "Pratisthaa","982386321")
helper.fetch_all()