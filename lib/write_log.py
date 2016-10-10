# -*- coding: utf-8 -*-
import os
import time
 
def write_log(log):
    filePath = os.path.abspath(os.path.dirname(__file__))
    logFilePath = os.path.join(os.path.dirname(filePath),'log','log.txt')
    #print logFilePath
    execTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    open(logFilePath,'a').write(execTime+':'+log+'\n')