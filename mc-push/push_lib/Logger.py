# -*- coding: utf-8 -*-  

import os,sys
syspath=os.getcwd()[0:os.getcwd().find('AutoSMS')+8]
sys.path.append(syspath+'\\sms_config')
import logging  
import logging.config

import Config
  
LOG_FILENAME = 'logging.conf'
os.chdir(Config._WORKSPACE + "\\sms_config")
logging.config.fileConfig(LOG_FILENAME)
logger = logging.getLogger("running info")
