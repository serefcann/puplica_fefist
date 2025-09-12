import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import httpx
import asyncio
import json
df = pd.read_csv(r'C:\Users\şerefcanmemiş\Documents\projects_2\puplica\program_ids.csv')
id_list  = list(df.Column1)


# universite ve bolum id parametreleri
    
sem = asyncio.Semaphore(5)
async def fetch(url):
    async with sem:
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(url)
            if response.status_code != 200:
                raise Exception(f"Request failed with status {response.status_code}")
        return response.text
            
def parse_html(html_content):
    program_info = {}
    soup = BeautifulSoup(html_content.replace("---", "0"), 'html.parser')
    tables = soup.find_all('table', {'class':'table table-bordered'})
    program_info["Bölüm Adı"] = tables[0].find('th').text
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) == 2:
                key = cols[0].get_text(strip=True).replace('*','')
                value =cols[1].get_text(strip=True).replace('*','')
                program_info[key] = value
    return program_info

async def main(id_list):
    urls = id_list[0:100]
    tasks =[fetch(f'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1000_1.php?y={url}') 
            for url in urls]
    results = await asyncio.gather(*tasks)  
    parsed_data = [parse_html(html) for html in results]
    return parsed_data

parsed_data = asyncio.run(main(id_list))

with open ("yokatlas_data.json", 'w', encoding='utf-8') as f:
    json.dump(parsed_data, f, ensure_ascii=False, indent=3)


