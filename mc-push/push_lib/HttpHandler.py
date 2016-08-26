# -*- coding: utf-8 -*-
'''
Created on 2015年6月16日

@author: gaoweiwei
'''
import os,sys
import requests
import Logger
syspath=os.getcwd()[0:os.getcwd().find('AutoSMS')+8]
sys.path.append(syspath+'\\sms_log')

class HttpHandler(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def request(self,api,case):
        try:
            url=api['apiurl']
            method=api['apimethod']
            data={}
            for i in range(len(api['apiprams'])):
                data[api['apiprams'][i]]=case[api['apiprams'][i]]
        except Exception,e:
            print e
            Logger.logging.error(e)
        try:
            if method=='GET':
                res=requests.get(url,params=data)
            if method=='POST':
                res=requests.post(url,data=data)
            else:
                'ERROR: only GET or POST allowed'
            return res
        except Exception,e:
            #print 'ERROR occured while sending the request'
            return -1
        
    
   
if __name__=='__main__':
    
    '''
    api={'url': 'http://cp01-tuangou-qa02.cp01.baidu.com:8588/mc-sms/sms/phone.json', 'method': 'POST'}
    req=ReqHandler()
    res2=req.request(api,params[0])
    print res2.json()
             
        try:
            url=api['url']
            method=api['method']
        except Exception,e:
            print 'ERROR while parsing request params'
            return -1
        if method=='GET':
            r=requests.get(url, params=case)
        elif method=='POST':
            r=requests.post(url,data=case)
        return r
        '''