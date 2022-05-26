# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:27:44 2020

@author: rajeshkanna
"""
import os, sys
import re
import time
import glob
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.options import Options
attempt = 0

user = 'xxxxxxxxxxxx'
pwd =  'xxxxxxxxxxxxx'
bktitle = "CHARITIES Vol"
#user = sys.argv[1]
#pwd =  sys.argv[2]
downpath = sys.argv[1]
#bktitle = sys.argv[2]

#downpath = r'D:\python\Scrapers\Relix_scraper\non-scrapy\testing'

def filerename(fname, attempt):
    alist = glob.glob(downpath + "/" + "*[0-9]+.HTML")
    if len(alist) == 0 and attempt < 20:
        time.sleep(2)
        attempt = attempt + 1
        filerename(fname,attempt)
    for file in os.listdir(downpath):
        if file.lower().endswith('.html'):
            updatedname = re.sub(r"(\-[0-9]+)(\.html)", "\\1_" + fname + "\\2", file, 0, re.MULTILINE | re.IGNORECASE)
            if fname in updatedname:
                os.rename(os.path.join(downpath, file), os.path.join(downpath, updatedname))
                #print('Saving ' + fname + 'Completed')


def downloadfile(key):
    print('Downloading ' + key)
    driver.find_elements_by_xpath('//*[@id="delivery_DnldRender"]')[0].click()
    time.sleep(2)
    if key == 'TOC':
        driver.find_elements_by_xpath('//*[@id="delView"]/option[@value="GNBEXLIST"]')[0].click()
        driver.find_elements_by_xpath('//*[@id="ui-id-4"]')[0].click()
        time.sleep(1)
    else:
        driver.find_elements_by_xpath('//*[@id="delView"]/option[@value="GNBFULL"]')[0].click()
        driver.find_elements_by_xpath('//*[@id="ui-id-9"]')[0].click()
        time.sleep(1)

    driver.find_elements_by_xpath('//*[@id="delFmt"]/option[@value="QDS_EF_HTML"]')[0].click()
    time.sleep(1)
    driver.find_elements_by_xpath('//a[@class="deliverBtn"]')[0].click()
    element = WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="closeBtn"]/img'))
        )
    time.sleep(2)
    driver.find_elements_by_xpath('//*[@id="closeBtn"]/img')[0].click()

#relpath = os.path.realpath(__file__)
#reldir = os.path.dirname(relpath)
reldir = os.path.dirname(__file__)
driverexe = os.path.join(reldir, 'Driver', 'chromedriver.exe')
#relpath = r'D:\python\Scrapers\Relix_scraper\relix\relix\spiders'
#driverexe = os.path.join(relpath, 'Driver', 'chromedriver.exe')

options = webdriver.ChromeOptions() 
prefs = {'download.default_directory' : downpath}
options.add_experimental_option('prefs', prefs)

#options.add_argument('headless')
#options.add_argument('window-size=1200,1100')
driver = webdriver.Chrome(executable_path=driverexe, options=options)
#driver = webdriver.Chrome(executable_path=driverexe)


driver.get("https://www.lexisnexis.com/uk/legal/auth/signonform.do?type=2")
print('Started login Process')
time.sleep(1)
element = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="webId"]'))
    )
#driver.find_element_by_id("webId").send_keys('kavitakrishnan')
#driver.find_element_by_id("password").send_keys('march_08')
driver.find_element_by_id("webId").send_keys(user)
driver.find_element_by_id("password").send_keys(pwd)
driver.find_elements_by_xpath('//*[@id="signInSubmit"]')[0].click()

print('Crawling Commentary Section')
element = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="secondarytabs"]/ul/li[4]/a'))
    )
driver.find_elements_by_xpath('//*[@id="secondarytabs"]/ul/li[4]/a')[0].click()
element = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="searchTextAreaStyleMSinput"]'))
    )

print('Searching ' + bktitle)

driver.find_element_by_id("searchTextAreaStyleMSinput").click()
time.sleep(2)

# to avoid sendkeys mistake we are inserting word by word
print('Searching the Article List')
titlelist = bktitle.split(' ')
for idx, eitem in enumerate(titlelist):
    if idx == 0:
        driver.find_element_by_id("searchTextAreaStyleMSinput").send_keys(eitem)
    else:
        time.sleep(1)
        driver.find_element_by_id("searchTextAreaStyleMSinput").send_keys(' ' + eitem)

#driver.find_element_by_id("searchTextAreaStyleMSinput").send_keys(bktitle)
#time.sleep(1)
driver.find_elements_by_xpath('//*[@id="sourceSelectDDStyle"]/option[22]')[0].click()
driver.find_elements_by_xpath('//*[@id="enableSearchImg"]')[0].click()

element = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="delivery_DnldRender"]'))
    )
time.sleep(1)

# Download Function
downloadfile('TOC')
print('Saving TOC')
filerename('TOC',attempt)
downloadfile('FULLTXT')
print('Saving FULLTXT')
filerename('FULLTXT',attempt)
time.sleep(1)
print('Process completed')
driver.close()

#print(download_wait(downpath))



