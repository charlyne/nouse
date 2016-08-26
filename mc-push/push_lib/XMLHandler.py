# -*- coding: utf-8 -*-
'''
Created on 2015年6月29日

@author: gaoweiwei
'''
import os,sys,string
import  xml.dom.minidom
from xml.etree import ElementTree as ET 
syspath=os.getcwd()[0:os.getcwd().find('AutoSMS')+8]

class XMLHandler(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        
    def load_parm_xml(self,xmlfile=''):
        paramList=[]
        try:
            tree=ET.parse(xmlfile)
            root=tree.getroot()
        except Exception, e:
            print "Error: cannot parse file: "%xmlfile
            return -1
        api_node=root.find('api')
        childs=api_node.getchildren()
        for child in childs:
            grandchilds=child.getchildren()
            #print child.tag
            for gchild in grandchilds:
                paramList.append(gchild.tag)
                #print gchild.tag
                
            
        return paramList    
        
        '''
        dom=xml.dom.minidom.parse(xmlfile)
        root=dom.documentElement
        print root.firstChild.nodeName
        for m in root.childNodes:
            child=m[0].firstChild
            print child.nodeName
            print child.nodeType
        print root.nodeName
        print root.nodeType
        print root.ELEMENT_NODE
        '''
        
if __name__=='__main__':
    text=syspath+'\sms_config\HandShake.api.xml'
    #print text
    xmlh=XMLHandler()
    list=xmlh.load_parm_xml(text)
    print list