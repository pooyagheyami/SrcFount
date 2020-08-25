# In the name of God
#! use/bin/env python

import sqlite3
import os


class WXDB(object):
    def __init__(self,database=":memory:",pathdb=os.getcwd()):
        self.database=pathdb+"\\"+database
        #print( self.database)
        self.connect()

    def connect(self):
        #print self.database
        try :
           self.connection=sqlite3.connect(self.database)
           self.cursor=self.connection.cursor()
        except:
           print("No Database found")
        self.connected=True
        self.statement=''
        return self.connection

    def close(self):
        self.connection.commit()
        self.connection.close()
        self.connected=False


    def commit(self):
        return self.connection.commit()
        
    def execute(self,statments):
        #with self.connect():
        self.cursor.execute(statments)
        result = self.cursor.fetchall()
        return result
    
    def execone(self,statments,*data):
        #with self.connect():
        #print( statments , data , data[0])
        #print data,data[0],data[0][0]
        if data == None:
            self.cursor.execute(statments)
        else:
            self.cursor.execute(statments,data[0])
        result = self.cursor.fetchall()
        #print result
        return result 

class SQLite(object):
    def __init__(self,tabels,fields,values):
        self.tabels=tabels
        self.fields=fields
        self.values=values

    def create(self,**karg):
        pass

    def insert(self,**karg):
        sql = 'insert into '+str(self.tabels)
        sql = sql+ '('+str(self.fields)+')'
        
        
        sql = sql +' values '+'('+'?,'*(len(self.fields.split(','))-1)+'?)'
        
        #print sql
        return sql

    def select(self,*arg,**karg):
        
        sql =  ' select '+self.fields+' from '+self.tabels
        #print sql
        return sql

    def select1(self,*arg,**karg):
        
        sql =  ' select distinct'+self.fields+' from '+self.tabels+' where '+self.values
        #print sql
        return sql

    def update(self,**karg):

        sql = ' update '+self.tabels+' set '+self.fields
        #print sql
        return sql

    def delete(self,**karg):
        sql = ' delete from '+self.tabels+' where '+self.values
        return sql
    
def MyDB_Path(database):
    return WXDB(database)


def wxsqsel(database,tabels,fields='*',condition=''):

    Mydb = MyDB_Path(database)
    Mydb.connect()
    sql = SQLite(tabels,fields,condition)
    sql1 = sql.select(fields,tabels)
       
    mylist = Mydb.execute(sql1)
    return mylist

def wxsqsel1(database,tabels,fields='*',condition=''):

    Mydb = MyDB_Path(database)
    Mydb.connect()
    sql = SQLite(tabels,fields,values=condition)
    sql1 = sql.select1(fields,tabels,values=condition)
    #print sql1   
    mylist = Mydb.execute(sql1)
    return mylist

def wxsqltxt(database,text):
    #global MAP
    Mydb = MyDB_Path(database)
    mylist = Mydb.execute(text)
    return mylist
    
def wxsqins(database,tabels,fields,data):
    #global MAP
    Mydb = MyDB_Path(database)
    sql = SQLite(tabels,fields,values=data)
    sql1 = sql.insert()
    #print sql
    mylist = Mydb.execone(sql1,data)
    Mydb.commit()
    Mydb.close()
    #print mylist
    return mylist
    
def wxsqlup(database,tabels,fields,data):
    #global MAP
    Mydb = MyDB_Path(database)
    sql = SQLite(tabels,fields,values=data)
    sql1 = sql.update()
    #print sql
    #print sql1
    mylist = Mydb.execone(sql1,data)
    Mydb.commit()
    Mydb.close()
    #print mylist
    return mylist 

def wxsqdel(database,tabels,data):
    #global MAP
    Mydb = MyDB_Path(database)
    sql = SQLite(tabels,fields='',values=data)
    sql1 = sql.delete()
    #print sql
    #print sql1
    mylist = Mydb.execute(sql1)
    Mydb.commit()
    Mydb.close()
    #print mylist
    return mylist

def wxsqsnd(database,tabel,field1,field2,data):
    #global MAP
    Mydb = MyDB_Path(database)
    mylist = Mydb.execute('select '+tabel+'.'+field1+' from '+tabel+' where '+tabel+'.'+field2+" = '%s' "%data)
    #print mylist
    return mylist
