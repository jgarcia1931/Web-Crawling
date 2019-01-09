from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import urlopen


url = 'https://weedmaps.com/brands/all?page=1'

# Getting the webpage, creating a Response object.
# response = requests.get(url).text
# response = urlopen("https://www.python.org/")
response = urllib2.urlopen(url)


# Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
soup = BeautifulSoup(response.read(), 'html5lib')

print(soup.prettify())

art = soup.find('div')
# print(art)

test = soup.find_all(class_='table-cell')
print(test)


body = soup.find('ion-nav-view')




# headers = {'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
# r = requests.get('https://weedmaps.com/brands/all?page=1', headers=headers)
#
# # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
# soup = BeautifulSoup(r.read(), 'html5lib')
#
# print(soup.prettify())