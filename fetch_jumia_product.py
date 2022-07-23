import requests
from bs4 import BeautifulSoup

#iphone 7 link
iphone7_link = 'https://www.jumia.com.ng/apple-renewed-iphone-7-plus-32gbram3gb-black-iphone7p-118774089.html'

#iphone 8 link
iphone8_link='https://www.jumia.com.ng/apple-renewed-iphone-8-64gb3gb-ram-gold-iphone8-102114632.html'

#Just add the product link here and fetch the price

def fetch_jumia_product(product_link):
    jumia_product_url= product_link
    page = requests.get(url=jumia_product_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('span', class_='-b -ltr -tal -fs24').text
    phone={
        'price':price
    }
    return phone["price"]




print(fetch_jumia_product(iphone7_link))
print(fetch_jumia_product(iphone8_link))

