from bs4 import BeautifulSoup
import requests



source = requests.get('https://www.jumia.com.ng/macbooks/').text 

soup = BeautifulSoup(source, 'lxml')

for laptop in soup.find_all('div', class_="info"):
    laptop_model = laptop.h3.text
    laptop_price = laptop.find('div', class_="prc").text
    
    print(f"Model: {laptop_model}, \t Price: {laptop_price}")