# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 13:30:09 2022

@author: rajeshkanna
"""

import os, re

# filereading
with open(r'D:\GitHub\Personal\Python-Programs\open\fire.csv', 'r') as txtfile:
    filecont = txtfile.read()
    txtfile.close()

#content modification
result = re.sub(r"^\"\"\,([0-9]+\,)", "\\1", filecont, 0, re.MULTILINE)


# filesaving
file = open(r'D:\GitHub\Personal\Python-Programs\open\fire.csv','w') 
file.write(result)
file.close()