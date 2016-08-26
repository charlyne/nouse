# -*- coding: utf-8 -*-
'''
Created on 2015年9月6日

@author: gaoweiwei

'''
# 搞了半天，不能把方法名和true直接assert
import pytest
import sys,os
syspath=os.getcwd()[0:os.getcwd().find('AutoSMS')+8]
sys.path.append(syspath+'\sms_api')
sys.path.append(syspath+'\sms_lib')
sys.path.append(syspath+'\sms_cases')
from SmsAPI SmsAPI1 SmsApi

#l = [["foo", "a", "a",], ["bar", "b", "b"], ["lee", "b", "b"]]
#print l
l=SmsApi('upLinkCallback')
@pytest.mark.parametrize('apicase', l.caselist)

def test_upLinkCallback(apicase):
    print apicase
        
    mm=l.get_res(apicase)
    #print mm['act_rs'].json()
    rs=l.judge_res(mm)
    print 'the act result is:'
    print mm['act_rs']
    print('r\n')
    print 'the exp result is:'
    print mm['exp_rs']
    assert rs==True,mm['desc']
    
