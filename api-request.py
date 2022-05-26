# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 19:50:04 2020

@author: rajeshkanna
"""

import requests

url = "http://10.0.00.00/Controller/schematronApi.php"

payload = [{'request_id': 'wijwdc96175b0747282229093c58a75e', 'html_filename': 'mye_9781319132101_prologue_03.xhtml', 'schema_version': '', 'timestamp': 1595229674, 'status': '', 's3_url': 'https://bs-frost-validator-s3-schematron-dev.s3.amazonaws.com/input/6762/wijwdc96175b07475e/my_19132101_prole_03.xhtml', 'callback_api': 'https://learning.com/frost/api/public/api/v1/report?access_token=fbcd2bcedda3cc470c4168edad5131571f8e78cc'}]

headers = {
    'authorization': "Bearer eyJbGciOiJIUzI1NiJ9.eyJpc3MiRElFTkNFIiwiaWF0IjoxNTk0Mzc2MzM4LCJkYXRhIjp7ImlkIjoxLCJlbWFpbCI6Ijk1MTcyOTIxMjk0MDQ3MjI0ODg0In19.L-NAhZ3YvQjSe6GQ1n3vc",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "befd-2fb-fcsa-ssa5-df8df123462"
    }

response = requests.request("POST", url, data=json.dumps(event).encode('utf-8'), headers=headers)

print(response.text)

    