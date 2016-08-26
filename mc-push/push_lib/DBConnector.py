# -*- coding: utf-8 -*-

'''
Created on 2015年5月7日

@author: gaoweiwei
'''
import os,sys
syspath=os.getcwd()[0:os.getcwd().find('AutoSMS')+8]
sys.path.append(syspath+'\\sms_config')
import Config
import MySQLdb
class DBConnector(object):
    '''
    classdocs
    '''
    connector=None


    def __init__(self):
        '''
        Constructor
        '''
        db_addr=Config.sms_db
        self.connector=MySQLdb.connect(db=db_addr['db'],host=db_addr['host'],user=db_addr['user'],passwd=db_addr['passwd'],port=db_addr['port'],charset='utf8')
        
        #cf=ConfigParser.ConfigParser()
        #cf.read(params)
        #addr=cf.items("sms_db")
        #self.dbConnector=MySQLdb.connect(Config=addr.get('Config'),host=addr.get('host'),user=addr.get('user'),passwd=addr.get('passwd'))
        
        
    def selct(self,query):
        cur=self.connector.cursor()
        cur.execute(query)
        db_rs=[]
        for data in cur.fetchall():
            db_rs.append(data)
        return db_rs
    
    def delclean(self):
        pass
        
if __name__ == "__main__":
    ll=DBConnector() 
    cur = ll.connector.cursor()
    cur.execute('show databases;')
    for dta in cur.fetchall():
        print dta
        
        
        
        