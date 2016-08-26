# -*- coding: utf-8 -*-
'''
Created on 2015年6月15日

@author: gaoweiwei
'''
import os,sys,string
import csv
import Logger
syspath=os.getcwd()[0:os.getcwd().find('AutoSMS')+8]
class CSVHandler(object):
    '''
    classdocs
    '''
    #case_list=[]

    def __init__(self):
        pass
        '''
        Constructor
        '''
    def readCSV(self,filepath=''):
        case_list=[]
        try:
            for line in csv.DictReader(open(filepath,'rb')):
                case_list.append(line)
                #print line
            return case_list
        except Exception,e:
            Logger.logging.info(e)
                
    '''    
    def readCSV(self,filepath=''):
        self.case_list=[]
        #this is important,nor it will be wrong,when import CSVHander in other module, the CSVHander is the same
        #addres all the same
        
        try:
            with open(filepath,'rb') as f:
                reader = csv.reader(f)
                for row in reader:
                    if reader.line_num==1:
                        self.paramsName=row
                    else:
                        #pass
                        self.dictlist(self.paramsName, row)
        except Exception,e:
            #print 'ERROR while load csvdata%s'%(e)
            Logger.logging.error("read cases from csv failed")
            Logger.logging.error(e)
            return []
        return self.case_list
    '''
    def dictWriter(self):
        pass
    
    def dictlist(self,lkeys,lvalues):
        paramsdict={}
        if len(lkeys)!=len(lvalues):
            pass
        else:
            for i in range(len(lkeys)):
                paramsdict[lkeys[i]]=lvalues[i]
        self.case_list.append(paramsdict)  
        print  paramsdict                
    
if __name__ == '__main__':
    filepath=syspath+'/sms_data/case/egg2.csv'
    tt=CSVHandler()
    tt.readCSV(filepath)
    print tt.case_list