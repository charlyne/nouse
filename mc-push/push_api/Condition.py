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
_APICASE=_WORKSPACE+'\\sms_cases\\condition.conf'

#single post request 
class Condition(unittest.TestCase):
    def setUp(self):
        self.api=SmsAPI("condition")
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
if __name__ == "__main__":
    report_title = u'E'
    desc = u'tRunner'
    filename = 'D:\\ExampleReport1.html'
    testsuite = unittest.TestSuite()
    testsuite.addTest(Condition("test_case1"))
    #testsuite.addTest(Condition("test_case2"))
    #testsuite.addTest(Condition("test_case3"))
    #testsuite.addTest(Condition("test_case4"))

    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  
    runner.run(testsuite) 
    
    #unittest.main()
