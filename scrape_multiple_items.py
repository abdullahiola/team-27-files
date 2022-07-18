import requests
from bs4 import BeautifulSoup


def scrape(keyword):
    jumia_product_url=f"https://www.jumia.com.ng/catalog/?q={keyword}"
    headers = {"user-agent":"Mozilla/5.0 (Linux; Android 10; TECNO CD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.114 Mobile Safari/537.36"}
    page = requests.get(url=jumia_product_url,headers=headers)
    soup=BeautifulSoup(page.content,'lxml')
    price = soup.select('.prc')
    first_prices = price[0]
    return first_prices

def extract(jeyword):
    scrapedword=str(scrape(jeyword))

    print(scrapedword)


extract('iphone11')

# [int(s) for s in str.split() if s.isdigit()