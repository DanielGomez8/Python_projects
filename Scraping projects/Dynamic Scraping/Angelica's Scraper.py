# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 13:04:51 2018

@author: Daniel
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://portal.gdc.cancer.gov/cases/2b5ef82d-e137-43f6-bfef-b202f20ee187?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A[%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.demographic.race%22%2C%22value%22%3A[%22white%22]%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.disease_type%22%2C%22value%22%3A[%22Adenomas%20and%20Adenocarcinomas%22]%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A[%22TCGA-PRAD%22]%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22files.data_format%22%2C%22value%22%3A[%22VCF%22]%7D%7D]%7D'
driver = webdriver.Chrome(executable_path='D:\programin\Drivers\chromedriver.exe')

driver.get(url)

# wait for element to appear, then hover it
try:
    element = EC.visibility_of_element_located((By.XPATH, "//div[@class='test-tab']"))
    WebDriverWait(driver, 20).until(element)
except:
    print('error')

res = driver.page_source

f = open('test.txt','w')
f.write(res)
f.close()

element = driver.find_element_by_xpath("//*[contains(text(),'Diagnoses / Treatments')]")
element.click()
res = driver.page_source
f = open('test2.txt','w')
f.write(res)
f.close()

driver.quit()


