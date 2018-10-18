# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:23:55 2018

@author: Daniel
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
import re

url = 'http://www.ciudadjuarez.com/directorio/3'
records = []

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('div', attrs={'class' : 'post'})
for result in results:
    try:
        name = result.find('span', attrs='post-title').text
        address = result.find('span', attrs='post-address').text[11:].replace('\t','')
        phone = result.find('span', attrs='post-telephone').text
        item = (name,address,phone)
        if not item in records:
            records.append(item)
    except:
        print('error')

for record in records:
    print(record)