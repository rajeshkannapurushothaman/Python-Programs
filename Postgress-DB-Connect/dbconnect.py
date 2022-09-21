# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:54:14 2022

@author: rajeshkanna
"""

import psycopg2
from sshtunnel import SSHTunnelForwarder
import paramiko

key=paramiko.RSAKey.from_private_key_file(r'D:\app-new1')

try:

    with SSHTunnelForwarder(
         ('52.xxx.16.xxx', 22),
         ssh_pkey=key,
         ssh_username="app-admin",
         remote_bind_address=('xxxx.xxxxxxxx.us-east-1.rds.amazonaws.com', 5432)) as server:
         
         server.start()
         print("server connected")

         conn = psycopg2.connect(user = "app-admin",
                                    password = "xxxxxxxxx",
                                    host = "xxxx.xxxxxxxxx.us-east-1.rds.amazonaws.com",
                                    #host = '10.0.0.81',
                                    port = "5432",
                                    database = "live")
         #cursor = conn.cursor()

         print("database connected")

except :
    print("Connection Failed")

