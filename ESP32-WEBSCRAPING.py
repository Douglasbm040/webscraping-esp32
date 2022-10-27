import requests
from bs4 import BeautifulSoup
import time 


html = requests.get("https://www.espressif.com/en/products/modules/esp32")
soup = BeautifulSoup(html.text,'html.parser')
html = soup.prettify()
print(html)