'''
@author: gaoweiwei
'''
#coding=utf-8
import sys,os
import json
import unittest
from SmsAPI import SmsAPI
import HTMLTestRunner
_WORKSPACE=os.getcwd()[0:os.getcwd().find('AutoSMS')+8]
sys.path.append(_WORKSPACE+'\\sms_lib')
_APICASE=_WORKSPACE+'\\sms_cases\\users.conf'

#single post request 
class Users(unittest.TestCase):
    def setUp(self):
        #get api's case
        self.api=SmsAPI("users")
        self.caselist=self.api.getCaseList()
        
    def tearDown(self):
        pass
    
    def test_case1(self):       
        act_rs=self.caselist[0]["act_rs"]
        exp_rs=eval(self.caselist[0]["exp_rs"])
        self.assertTrue(self.api.comparedRS(act_rs,exp_rs), act_rs)
    def test_case2(self): 
        act_rs=self.caselist[1]["act_rs"]
        exp_rs=eval(self.caselist[1]["exp_rs"])
        self.assertTrue(self.api.comparedRS(act_rs,exp_rs), act_rs)
    def test_case3(self): 
        act_rs=self.caselist[2]["act_rs"]
        exp_rs=eval(self.caselist[2]["exp_rs"])
        self.assertTrue(self.api.comparedRS(act_rs,exp_rs), act_rs)
    def test_case4(self): 
        act_rs=self.caselist[3]["act_rs"]
        exp_rs=eval(self.caselist[3]["exp_rs"])
        self.assertTrue(self.api.comparedRS(act_rs,exp_rs), act_rs)

    
    #unittest.main()
