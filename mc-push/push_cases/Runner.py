'''

@author: gaoweiwei
'''
import sys,os
import json
import unittest
from SmsAPI import SmsAPI
from Single import Single
from HandShake import HandShake
from Groupid import Groupid
from Users import Users
from Condition import Condition
import HTMLTestRunner
_WORKSPACE=os.getcwd()[0:os.getcwd().find('AutoSMS')+8]
sys.path.append(_WORKSPACE+'\\sms_lib')
_APICASE=_WORKSPACE+'\\sms_cases\\single.conf'

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()

    testsuite = unittest.TestSuite()
    testsuite.addTest(Groupid("test_case1"))
    testsuite.addTest(Groupid("test_case2"))
    testsuite.addTest(Groupid("test_case3"))
    testsuite.addTest(HandShake("test_case1"))
    testsuite.addTest(HandShake("test_case2"))
    testsuite.addTest(HandShake("test_case3"))
    testsuite.addTest(HandShake("test_case4"))
    testsuite.addTest(Single("test_case1"))
    testsuite.addTest(Single("test_case2"))
    testsuite.addTest(Single("test_case3"))
    testsuite.addTest(Single("test_case4"))
    testsuite.addTest(Single("test_case5"))
    testsuite.addTest(Single("test_case6"))
    testsuite.addTest(Users("test_case1"))
    testsuite.addTest(Users("test_case2"))
    testsuite.addTest(Users("test_case3"))
    testsuite.addTest(Users("test_case4"))
    testsuite.addTest(Condition("test_case1"))
    filename = 'D:\\ExampleReport1.html'
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'Report_push ',description='Report_description')  
    runner.run(testsuite) 