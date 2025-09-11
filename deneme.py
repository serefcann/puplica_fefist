import requests
from bs4 import BeautifulSoup
import pandas as pd
df = pd.read_csv(r'C:\Users\şerefcanmemiş\Documents\projects_2\puplica\program_ids.csv')
id_list  = list(df.Column1)
id_list[0]
# universite ve bolum id parametreleri
for ids in id_list[:10]:
    url = f'https://yokatlas.yok.gov.tr/lisans.php?y={ids}'
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    soup.prettify()
    # Örnek: Üniversite adı
    uni_name = soup.find('h3').text.strip()
    print(f"Üniversite Adı: {uni_name}")




