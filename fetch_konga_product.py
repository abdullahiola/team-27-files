import requests
from bs4 import BeautifulSoup

#test product link
productlink1='https://www.konga.com/product/iphies-permanent-pink-lips-magic-cream-3days-active-20ml-5524323'

#iphone 7 link
iphone7_link='https://www.konga.com/product/apple-iphone-7-128gb-rom-2gb-ram-black-back-case-screen-protector-and-power-bank-5197083'


# iphone 8 link
iphone8_link='https://www.konga.com/product/apple-iphone-8-4-7inch-64gb-rom-2gb-ram-5695912'

def fetch_konga_product(link):
    konga_product_url=link
    page = requests.get(url=konga_product_url)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find('div', class_="_678e4_e6nqh")
    return price.get_text()

print(fetch_konga_product(productlink1))
print(fetch_konga_product(iphone7_link))
print(fetch_konga_product(iphone8_link))

