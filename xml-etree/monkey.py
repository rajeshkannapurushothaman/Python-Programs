# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 12:27:21 2022

@author: rajeshkanna
"""
import lxml.etree as ET
import re

import os

inputdir = r"D:\Monkey\cleanup\100_QA_Alias"

dirlist = os.listdir(inputdir)

fullist = ['Alias,Filename,DOCid,Problematic Entity']

for infolder in dirlist:
    eachfolder = os.path.join(inputdir, infolder)
    for file in os.listdir(eachfolder):
        entgoal = os.path.join(inputdir, eachfolder, file)
        
        etgl = ET.parse(entgoal)
        etglroot = etgl.getroot()
        
        entdoctext = {}
        
        for upelement in etglroot:
            updatext = str(ET.tostring(upelement))
            docidtxt = re.search(r"<SET_DOC ID=\"(\d+)\"", updatext, re.MULTILINE)
            entityrst = re.findall(r"&\#[0-9]{5,}\;", updatext)
            docvalue = ''
            if docidtxt:
                docvalue=docidtxt.group(1)
            if entityrst:
                if docvalue != '':
                    entdoctext[docvalue] = entityrst
                    fullist.append(str(infolder)+ ',' + str(file) + ',' + str(docvalue) + ',' + ' '.join(entityrst))
                    
file = open(os.path.join(inputdir, '100_QA_Alias.csv'), 'w')
file.writelines("% s\n" % data for data in fullist)
file.close()


    