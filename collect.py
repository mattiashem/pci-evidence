#!/usr/bin/env python
#
#
# file to collect info about system and store in output file
#

import os
import sys
import evidence

def run():
    '''
    Open all files in the evidence folder and run all run() functions to get evidence output
    '''
    for filename in os.listdir('evidence'):
        if filename =='__init__.py' or filename[-3:] != '.py':
            pass
        else:
            eval('evidence.'+filename[:-3]+'.run()')
           
run()
