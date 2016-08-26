#/usr/bin/python
 # -*-coding:utf-8 -*-
import ConfigParser
import string, os, sys
 
cf = ConfigParser.ConfigParser()
 
cf.read("duty.conf")
 
#return all section
secs = cf.sections()
print 'sections:', secs
#cc=cf.get("3duan","3duan_watcher")
#print 'cc' ,cc
 
#opts = cf.options("handler_consoleHandler")
#print 'options:', opts
 
#kvs = cf.items("db")
#print 'db:', kvs

for i in range(len(secs)):
    kvs = cf.items(secs[i])
    print secs[i],kvs
    for j in range(len(kvs)):
        print kvs[j][0], kvs[j][1]
    
    