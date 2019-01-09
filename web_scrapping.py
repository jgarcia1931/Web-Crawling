import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


store_list = []

# 56 is the number of pages the website has
for page in range(1,56):
    print("store " + str(page))

    # This is the path of the Chrome executable file
    # This is the file that launches Chrome
    driver = webdriver.Chrome(executable_path='exec_path')
    url = "web_site_url" + str(page)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    test = soup.find_all(class_='table-cell')
    items = len(test)

    for i in range(items):
        testing = test[i]
        spans = testing.find_all('span')
        web_link = spans[0].string
        store_name = spans[1].string
        store_list.append([store_name, web_link])

store_series = pd.DataFrame(store_list, columns=['Store_Name', 'Web_Link'])
store_series.to_csv('store_list.csv')

