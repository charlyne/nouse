# test_math.py
import sys,os
_WORKSPACE=os.getcwd()[0:os.getcwd().find('AutoSMS')+8]
sys.path.append(_WORKSPACE+'\\sms_lib')
from nose.tools import assert_equal
from nose_parameterized import parameterized
from SmsAPI import SmsAPI
_A=1.0
import unittest
import math
import HTMLTestRunner

caselist=SmsAPI("handshake").getCaseList()
class TestMathUnitTest(unittest.TestCase):
    @parameterized.expand([
        #(caselist[0]["name"],caselist[0]["exp_rs"],caselist[0]["exp_rs"]),
        ("22","act_rs","exp_rs"),
    ])
    def test_floor(self, name, input, expected):
        assert_equal(input, expected)

    def setUp(self):
        #get api's case
        self.api=SmsAPI("handshake")
        self.caselist=self.api.getCaseList()  
    def test_handshake(self):
        pass
if __name__ == '__main__':  
    report_title = u'E'
    desc = u'tRunner'
    filename = 'D:\\ExampleReport.html'
    testsuite = unittest.TestSuite()
    testsuite.addTest(TestMathUnitTest("test_handshake"))
    testsuite.addTest(TestMathUnitTest("test_floor"))
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  
    runner.run(testsuite) 