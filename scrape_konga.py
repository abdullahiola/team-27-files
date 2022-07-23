import requests
from bs4 import BeautifulSoup


def scrape(keyword):
    konga_product_url=f"https://www.konga.com/search?search={keyword}"
    headers = {"user-agent":"Mozilla/5.0 (Linux; Android 10; TECNO CD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.114 Mobile Safari/537.36"}
    page = requests.get(url=konga_product_url,headers=headers)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find("span", class_="d7c0f_sJAqi")
    price_text=price.next_sibling
    print(price.get_text())


scrape('iphone7')

