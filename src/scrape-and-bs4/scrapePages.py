from bs4 import BeautifulSoup
import requests
url = 'https://scrapingclub.com/exercise/list_basic/'
count = 1
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='w-full rounded border')
for i in items:
    itemName = i.find('h4').find('a').text
    itemPrice = i.find('h5').text
    print('%s) Price: %s , Item Name: %s' % (count, itemPrice, itemName))
    count = count + 1
pagination = soup.find('nav', class_='pagination')
pages = pagination.find_all('span', class_='page')
urls = []
for page in pages:
    if page.find('a') is not None and page.find('a').text.isdigit():
        pageNum = int(page.find('a').text) 
    else:
        continue
    #print(pageNum)
    link = page.find('a').get('href')
    urls.append(link)
for i in urls:
    response = requests.get(url + i)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='w-full rounded border')
    for i in items:
        itemName = i.find('h4').find('a').text
        itemPrice = i.find('h5').text
        print('%s) Price: %s , Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1