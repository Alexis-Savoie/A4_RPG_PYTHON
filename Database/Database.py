import mysql.connector

class Database:
    # Param object
    def __init__(self,user,password,host,database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.mydb = mysql.connector.connect(host = self.host, user = self.user,password = self.password, database = self.database)
        
    # Select where
    def select(self, element, table, where):
        if(where != ""):
            mycursor = self.mydb.cursor()
            sql = "SELECT "+element+" FROM "+table+" WHERE "+where
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            return myresult
        else:
            mycursor = self.mydb.cursor()
            sql = "SELECT "+element+" FROM "+table
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            return myresult
        
    # Insert data
    def insert(self, table, values, value):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO {} VALUES({})".format(table, values);
        val = value
        mycursor.execute(sql, val)
        self.mydb.commit()
        return mycursor.rowcount
    
    # update data
    def update(self,where,table, values, value):
        mycursor = self.mydb.cursor()
        sql = "UPDATE {} SET {} WHERE {}".format(table, values, where);
        val = value
        mycursor.execute(sql, val)
        self.mydb.commit()
        return mycursor.rowcount
    
    # Isset variable in value null
    def isset(self, data):
        if data is None:
            return ""
        else:
            return data
        
    # Off connecte
    def disconnect(self):
        self.mydb.close()
