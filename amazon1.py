import requests
from bs4 import BeautifulSoup
from email_alert import alert_system



URL = "https://www.amazon.in/Samsung-Segments-Smartphone-Octa-Core-Processor/dp/B0BZCR6TNK/ref=sr_1_1_sspa?crid=1UKNU36ZJY8J9&keywords=mobiles%2Bunder%2B20000&qid=1706782901&sprefix=mobiles%2Bunder%2B20%2Caps%2C249&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}

set_price = 12000

def check_price():
    page= requests.get(URL, headers=headers)
    soup=BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    print(title)
    price= soup.find("span", class_='a-price-whole').get_text()
    
    product_price = " "
    for letters in price:
        if letters.isnumeric() or letters == ".":
            product_price+=letters
    print(float(product_price))

    if float(product_price) <= set_price:
        alert_system(title,URL)
        print('sent')
    else:
        print('not sent')

    

    

check_price()
