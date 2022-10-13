# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:35:24 2022

@author: rajeshkanna
"""

import lxml.etree as ET

textcont = '<p><b><b><i><b><i><b><i>sample text</i></b></i></b></i></b></b></p>'

soup = ET.fromstring(textcont)

for tname in ['i','b']:
    for tagn in soup.iter(tname):
        if tagn.getparent().getparent() != None and tagn.getparent().getparent().tag == tname:
            iparOfParent = tagn.getparent().getparent()
            iParent = tagn.getparent()
            if iparOfParent.text == None:
                iparOfParent.addnext(iParent)
                iparOfParent.getparent().remove(iparOfParent)
        elif tagn.getparent() != None and tagn.getparent().tag == tname:
            iParent = tagn.getparent()
            if iParent.text == None:
                iParent.addnext(tagn)
                iParent.getparent().remove(iParent)

            
print(ET.tostring(soup))
