import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
df = pd.read_csv(r'C:\Users\şerefcanmemiş\Documents\projects_2\puplica\program_ids.csv')
id_list  = list(df.Column1)
id_list[2]
# universite ve bolum id parametreleri
for ids in id_list[:10]:
    url = f'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1000_1.php?y={ids}'
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table', {'class':'table table-bordered'})

url = f'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1000_1.php?y={100110045}'
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

for ids in id_list[:10]:
    url = f'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1000_1.php?y={ids}'
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table', {'class':'table table-bordered'})
    program_info = {}
    tables = soup.find_all('table', {'class':'table table-bordered'})
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) == 2:
                key = cols[0].get_text(strip=True).replace('*','')
                value =cols[1].get_text(strip=True).replace('*','')
                program_info[key] = value
    program_info