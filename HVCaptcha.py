# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:10:02 2022

@author: rajeshkanna
"""

import requests,re
ses = requests.Session()
from twocaptcha import TwoCaptcha


twoCaptcha =TwoCaptcha('290c6e6b354234c3356af3523ff123')  # Your API key


captcha_token = twoCaptcha.recaptcha(sitekey='6LfGW7MeASFSDF7SDF9DOSDSFasdH',url='https://websiteurl.be/zoekmachine/zoekformulier') #Your site key need to insert in the sitekey attribute

print(captcha_token)

cookies = {
    'JUPORTAMODE': 'eNqFkUGOwjAMRe%2BSE7QMBWFWaWqaSG5cJalYcwFYsETcnSQFTWYqlWX%2Bf3bs7wvUO3jcof4BoZwJwaHSA3cojnfYg2iZCaVNrz8Ij%2BiSGDVpu2xvC9srdrlFDaJauGQGE5LagNg0VTUTTUHYcZR9brAB0cz%2BrvBbScScx6pALGxtyPQ6vOtv1wwcyvk0nx36acB1JmhU0n9lpjCtMwMHMu0600pP2Jcr%2FSdORmn0n9iJFsGy6%2BazxCx%2FT1Am06GPC6mkx8L0WmRP0vbTJxcbP3m%2BAGUtkjU%3D',
    'PHPSESSID': '8nj9113mqpmdjo2bh8d0nltdpl',
    'TS01dda8b2': '010e209861cd577e5832b4b201089f5952d8aadbacebc73750560d2b66397c248b5d2d8320af6304fe55f947b199a4e1c9f66d248c',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'JUPORTAMODE=eNqFkUsafsdafAMRe%2BSE7QMBWFWaWqaSG5cJalYcwFYsETcnSQFTWYqlWX%2Bf3bs7wvUO3jcof4BoZwJwaHSA3cojnfYg2iZCaVNrz8Ij%2BiSGDVpu2xvC9srdrlFDadsadsfsdasdfsdaadscZR9brAB0cz%2BrvBbScScx6pALGxtyPQ6vOtv1wwcyvk0nx36acB1JmhU0n9lpjCtMwMHMu0600pP2Jcr%2FSdORmn0n9iJFsGy6%2BazxCx%2FT1Am06GPC6mkx8L0WmRP0vbTJxcbP3m%2BAGUtkjU%3D; PHPSESSID=8nj9113mqpmdjo0nltasdfdsdpl; TS01dda8b2=010e209861cd5dasfdsaf233543089f5952d8aadbacebc73750560d2b66397c248b5d2d8320af6304fe55f947b199a4e1c9f66d248c',
    'Origin': 'https://juportal.be',
    'Pragma': 'no-cache',
    'Referer': 'https://websiteurl.be/zoekmachine/zoekformulier',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'latitude': '',
    'longitude': '',
    'accuracy': '',
    'altitude': '',
    'altitudeAccuracy': '',
    'g-recaptcha-response': captcha_token['code'],
    'TEXPRESSION': '',
    'TRECHTEXTE': 'on',
    'TRECHMOCLELIB': 'on',
    'TRECHRESUME': 'on',
    'TRECHNOTE': 'on',
    'TRECHLANGNL': 'on',
    'TRECHLANGFR': 'on',
    'TRECHLANGDE': 'on',
    'TRECHECLINUMERO': '',
    'TRECHNOROLE': '',
    'TRECHDECISIONDE': '2022-04-01',
    'TRECHDECISIONA': '2022-04-30',
    'TRECHPUBLICATDE': '',
    'TRECHPUBLICATA': '',
    'TRECHBASELEGDATE': '',
    'TRECHBASELEGNUM': '',
    'TRECHBASELEGART': '',
    'TRECHMODE': 'BOOLEAN',
    'TRECHOPER': 'AND',
    'TRECHSCORE': '0',
    'TRECHLIMIT': '25000',
    'TRECHNPPAGE': '50',
    'TRECHHILIGHT': 'on',
    'TRECHSHOWRESUME': 'on',
    'TRECHSHOWTHECAS': 'on',
    'TRECHSHOWTHEUTU': 'on',
    'TRECHSHOWMOTLIB': 'on',
    'TRECHSHOWFICHES': 'ALL',
    'TRECHORDER': 'SCORE',
    'TRECHDESCASC': 'DESC',
    'action': '',
}

response = requests.post('https://websiteurl/zoekmachine/zoekformulier', cookies=cookies, headers=headers, data=data)
print(response.status_code)
with open('tmp.html', 'w') as f:
    f.write(response.text)

