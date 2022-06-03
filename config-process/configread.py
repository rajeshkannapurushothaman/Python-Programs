# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:11:57 2019

@author: rajeshkanna
"""

import sys, os
import configparser

#configfile = sys.argv[1]
configfile = r'D:\python\configfilesteps\config.ini'
settings = configparser.ConfigParser()
settings.read(configfile)
settings.get('A','y')

