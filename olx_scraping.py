# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:18:20 2021

@author: hosam
"""

import selenium
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
browser = webdriver.Chrome(executable_path='C:/Users/hosam/Documents/Project/Olx scraping/chromedriver.exe')
def olx_search(Search):
    browser.get('https://www.olx.in/bengaluru_g4058803/q-'+Search+'?sorting=asc-distance')
    time.sleep(10)
    no_of_ads=int(browser.find_element_by_xpath("//span[@class='_3RsTo']").text.split(' ')[0])
    for a in range(0,no_of_ads//20):
        browser.find_element_by_xpath("//button[@data-aut-id='btnLoadMore']").click()
        time.sleep(5)
    soup=BeautifulSoup(browser.page_source,'lxml')
    
    a=soup.find_all('li','EIR5N')
    Final=[]
    for x in a:
        Link=Cost=Year=DistanceTravelled=Location=Title=''
        try:
            Link='https://www.olx.in'+x.find("a")['href']
        except AttributeError:
            pass
        try:
            Cost=x.find(attrs={"data-aut-id":"itemPrice"}).text
        except AttributeError:
            pass
        try:
            y=x.find(attrs={'data-aut-id':"itemDetails"}).text.split(' ')
            Year=y[0]
            DistanceTravelled=y[2]+' kms'
        except AttributeError:
            pass
        try:
            Location=x.find(attrs={"data-aut-id":"item-location"}).text
        except AttributeError:
            pass
        try:
            Title=x.find(attrs={'data-aut-id:'"itemTitle"}).text
        except AttributeError:
            pass
        Final.append([Search, Year, DistanceTravelled, Cost, Title, Location, Link])
    return Final

Search='Honda Shine'
final=olx_search(Search)
Data=pd.DataFrame(final, columns=['Item','Year', 'Distance Travelled','Cost', 'Title', 'Location', 'Link'])
    

    
