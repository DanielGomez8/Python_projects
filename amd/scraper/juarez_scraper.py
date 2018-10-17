import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
import re

records = []

def fix_phone(phone):
        phone = re.sub("\D", "", phone)
        if not phone[:3] == '656':
            phone = '656' + phone
        return phone[:10]

def url_reader(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        results = soup.find_all('div', attrs={'class' : 'post'})
        for result in results:
            try:
                name = result.find('span', attrs='post-title').text
                address = result.find('span', attrs='post-address').text[11:].replace('\t','')
                phone = fix_phone(result.find('span', attrs='post-telephone').text)
                item = (name,address,phone)
                if not item in records:
                    records.append(item)
            except:
                continue

page_num = int(input('Cantidad de Paginas: '))+1
sheet = input('Categoria: ')
page_index = input('indice de pagina: ')

url = 'http://www.ciudadjuarez.com/directorio/'+str(page_index)+'/'
url_reader(url)

for i in range(2,page_num):
        urlx = url + str(i)
        url_reader(urlx)

path = 'D:\programin\Python Scripts\AMD\JuarezBusiness.xlsx'



book = load_workbook(path)
writer = pd.ExcelWriter(path, engine = 'openpyxl')
writer.book = book

table = pd.DataFrame(records, columns=['Name','Address','Phone'])

table.to_excel(writer, sheet_name = sheet, index=False)
writer.save()
writer.close()

