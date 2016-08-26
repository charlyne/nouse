'''
Created on 2016-08-18

@author: gaoweiwei
'''
#coding=utf-8
import os,sys,json,time
import requests,ConfigParser
_WORKSPACE=os.getcwd()[0:os.getcwd().find('AutoSMS')+8]
sys.path.append(_WORKSPACE+'\\sms_config')
_APICONF =_WORKSPACE+'\\sms_config\\api.conf'
_CASECONF=_WORKSPACE+"sms_cases\\"
class SmsAPI(object):
    '''
    classdocs
    '''
    def __init__(self, apiname):
        '''
        Constructor
        '''
        cf=ConfigParser.ConfigParser()
        cf.read(_APICONF)
        self.apiname=apiname
        self.url=cf.get(self.apiname,"url")
        self.method=cf.get(self.apiname,"method")
        self.caselist=[]
    
    def request(self,data={}):
        #send request,and get response
        try:
            
            if(self.method=='GET'):
                res=requests.get(self.url,params=data)
                return res
            if(self.method=='POST'):
            #add header message
                headers = {'Content-Type': 'application/json'}
                res=requests.post(self.url,json=data,headers=headers)
                return res
        except Exception,e:
            return -1
        
    def getCaseList(self):
        #get this api's caselist, case like {"name":,"params":, "exp_rs"}
        filename=_CASECONF+self.apiname+".conf"
        cf1=ConfigParser.ConfigParser()
        cf1.read(filename)
        secs=cf1.sections()#cases
        caselist=[]
        for i in range(len(secs)):
            data={"name":"","params":{},"exp_rs":"","act_rs":{}}
            data["name"]=secs[i]
            opts=cf1.options(secs[i])
            for j in range(len(opts)):
                value=cf1.get(secs[i], opts[j])
                if(opts[j]=='exp_rs'):
                    data["exp_rs"]=value
                else:
                    data["params"][opts[j]]=value
            data["act_rs"]=self.request(data["params"]).json()
            caselist.append(data)
        return caselist
    def comparedRS(self,act_rs,exp_rs):
        try:
            if(act_rs["errno"]==exp_rs["errno"]):
                if(act_rs["msg"]==exp_rs["msg"]):
                    act_data=act_rs["data"]
                    exp_data=exp_rs["data"]
                    for k in exp_data.keys():
                        if exp_data[k]==".*":
                            continue
                        if exp_data[k]==act_data[k]:
                            continue
                        else:
                            return False
                    return True
                else:
                    return False
            else:
                return False
        except Exception:  
            return False
        
        

if __name__ == "__main__":
    api=SmsAPI("condition")
    list=api.getCaseList()
    headers = {'Content-Type': 'application/json'}
    url="http://cp01-tuangou-qa02.cp01.baidu.com:8588/mc-web/push/users.html"
    data={'info': '{}', 'src': 'mis', 'uids': '[3BA0E66DAC019D3CBFFD82BAEEEA6834|964641450506253]', 'title': 'autotest', 'utype': '1', 'pid': '128420', 'content': 'autotest', 'at': '0', 'et': '0', 'prod': '1', 'type': '3'}
    #for i in list:
      #  print i
       # res=requests.post(api.url,data=i["params"],headers=headers)
     #   print type(i["params"])
    res=requests.post(url=url,json=data,headers=headers)
    print res.json()
    
    #print api.getCaseList()

        
        
        
        