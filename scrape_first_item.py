import requests
from bs4 import BeautifulSoup


def scrape(keyword):
    jumia_product_url=f"https://www.jumia.com.ng/catalog/?q={keyword}"
    headers = {"user-agent":"Mozilla/5.0 (Linux; Android 10; TECNO CD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.114 Mobile Safari/537.36"}
    page = requests.get(url=jumia_product_url,headers=headers)
    soup=BeautifulSoup(page.content,'lxml')
    price =soup.find("span", class_="curr")
    price_text=price.get_text()
    print(price.get_text())


scrape('Nokia 3310')
scrape('iphone7')
scrape('samsung galaxy s10')
