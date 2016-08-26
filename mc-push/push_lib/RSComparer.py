# -*- coding: utf-8 -*-
'''
Created on 2015年7月6日

@author: gaoweiwei
'''
import json
class RSComparer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    def assert_rs(self,RS):
        try:
            compid=RS['t_assert']
            actrs=RS['t_act_rs'].json()
            exprs=json.loads(RS['t_exp_rs'])
            if(compid=='1'):
                if(RS['t_act_rs'].status_code!=200):
                    return False
                if(actrs['errno']!=(exprs['errno'])):
                    return False
                if(actrs['msg']==(exprs['msg'])):
                    return True
                return False
            else:
                print 'only compid=1 allowed'
        except Exception,e:
            pass   
            
        
        