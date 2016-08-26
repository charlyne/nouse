# -*- coding: utf-8 -*-
'''
Created on 2015年9月9日

@author: gaoweiwei
'''
import os,sys
syspath=os.getcwd()[0:os.getcwd().find('AutoSMS')+8]
sys.path.append(syspath+'\\sms_config')
sys.path.append(syspath+'\\sms_lib')
sys.path.append(syspath+'\\sms_log')
from DBConnector import DBConnector
filepath=syspath+'sms_log\\results.txt'
from DBConnector import DBConnector
class DBResulter(object):
    '''
    classdocs
    '''
    dbconnector=DBConnector()
    apihttprs=[]

    def __init__(self):
        '''
        Constructor
        '''
        self.dbconnctor=DBConnector()
    
    def read_http_rs(self):
        f=open(filepath,'a+')
        for line in open(filepath,'a+'):
            tmplist=line.split('@@@')
            #print type(tmplist[1])
            if (eval(tmplist[1])['isdeploydb']=='1'):
                #print type(tmplist[1])
                self.apihttprs.append(dict(apiname=tmplist[0],httprs=eval(tmplist[1])))
        return 0

    def test_db_rs(self,apihttprs):
        self.read_http_rs()
        if(apihttprs['apiname']=='phone') or (apihttprs['apiname']=='schedulePhone'):
            key=apihttprs['httprs']['act_rs']['data']['reqId']
            query='select * from bainuo_sms_req where req_id=\'%s'%(key)+'\''
            print query
            db_rs=self.get_dbrs(query)
            print db_rs
            if(len(db_rs)>0):
                apihttprs['db_rs']=db_rs
            else:
                apihttprs['db_rs']='FALSE'
            assert len(db_rs)>0
            ##################
        if(apihttprs['apiname']=='HandShake'):
            key=apihttprs['httprs']['act_rs']['data']['taskId']
            query='select * from bainuo_sms_task where id=\'%s'%(key)+'\''
            print query
            db_rs=self.get_dbrs(query)
            print db_rs
            if(len(db_rs)>0):
                apihttprs['db_rs']=db_rs
            else:
                apihttprs['db_rs']='FALSE'
            assert len(db_rs)>0
            
        
    def get_dbrs(self,query):
        return self.dbconnector.selct(query)
 
if __name__ == '__main__':
    db=DBResulter()
    print filepath
    db.read_http_rs()
    print db.apihttprs
    for i in range(len(db.apihttprs)):
        m=db.test_db_rs(db.apihttprs[i])
        print m
        
        
        