import requests
from bs4 import BeautifulSoup
import pandas as pd
df = pd.read_csv(r'C:\Users\şerefcanmemiş\Documents\projects_2\puplica\program_ids.csv')
# universite ve bolum id parametreleri

url = 'https://yokatlas.yok.gov.tr/lisans-univ.php?u=1072'
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')
soup.prettify()
# Örnek: Üniversite adı
uni_name = soup.find('h3').text.strip()
print(f"Üniversite Adı: {uni_name}")

print("hello world")


